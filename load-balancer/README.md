# Load Balancer
* A simple implementation of a Load Balancer. 
* There are three components to our program:
    * Server A
    * Server B
    * Load Balancer

## Steps to start
1. In the cloned directory, create a virtual environment: `virtualenv venv`

2. Enter the virtual environment: `source venv/bin/activate`

3. Install the dependencies: `pip install -r requirements.py`

4. Start Server A in one terminal: `python3 -m http.server [port-A]`

5. Start Server B in another terminal: `python3 -m http.server [port-B]`

6. Start the load balancer in another terminal: `python3 -m main`

## Using the program
Send a request to the load balancer, and watch how it switches b/w servers A and B

`curl [load_balancer_ip]:[load_balancer_port]`