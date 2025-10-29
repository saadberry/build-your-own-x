import socket
import threading

# Server data
backend_ip = "127.0.0.1"
server_port_1 = 9000
server_port_2 = 9001

# Loadbalancer data
loadbalancer_ip = "0.0.0.0"
loadbalancer_port = 8080

# List of available backend servers
backends = [
    (backend_ip, server_port_1),
    (backend_ip, server_port_2),
]

# ID of server to use
current = 0

def handle_client(client_socket, backend_address):
    """
    Method that handles a new client connection
    """
    try:
        backend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        backend_socket.connect(backend_address)

        threading.Thread(target=forward, args=(client_socket, backend_socket)).start()
        threading.Thread(target=forward, args=(backend_socket, client_socket)).start()

    except Exception as e:
        print(f"Error connecting to backend {backend_address}: {e}")
        client_socket.close()

def forward(source, destination):
    """
    Method that forwards data from source -> destination
    e.g. Client -> Server or Server -> Client
    """
    try:
        while True:
            data = source.recv(4096)
            if not data:
                break
            destination.sendall(data)
    except Exception:
        pass
    finally: 
        source.close()
        destination.close()

def start_load_balancer(host=loadbalancer_ip, port=loadbalancer_port):
    """
    Init Load Balancer
    """
    global current
    lb_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lb_socket.bind((host, port))
    lb_socket.listen(5)
    print(f"Load balancer listening on {host}:{port}")

    while True:
        client_socket, _ = lb_socket.accept()
        backend = backends[current]
        current = (current + 1) % len(backends)
        print(f"Forwarding new connection to {backend}")
        threading.Thread(target=handle_client, args=(client_socket, backend)).start()


if __name__ == '__main__':
    start_load_balancer()