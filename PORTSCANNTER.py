# scans the open ports on a target

# having open ports gives you vulnerability to attacks such as ddoses and whatnot.
# scan port with permission, not responsible.
# AF_INET is basically internet socket and not a Unix
import socket
import threading
from queue import Queue


victim = "default gateway / ip here"
queue = Queue()
ports_open = []


def portscanner(port):
    try:
        mainSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mainSock.connect((victim, port))
        return True
    except:
        return False


def fill_queue(list_of_ports):
    for port in list_of_ports:
        queue.put(port)


def workerport():
    while not queue.empty():
        port = queue.get()
        if portscanner(port):
            print("Port # {} is open and may be vulnerable.".format(portscanner))
    else:
            # remove lines 35 + 37 if you don't care about the closed ports
            print("Port # {} is closed and secured.".format(portscanner))
            ports_open.append(port)

list_of_ports = range(1, 1024) # ports 1-1024
fill_queue(list_of_ports)

list_of_threads = []

for th in range(10): # amount of threads 
    thread = threading.Thread(target=workerport)
    list_of_threads.append(thread)

for thread in list_of_threads:
    thread.start()

for thread in list_of_threads: 
    thread.join()

print("Your open ports are: ", ports_open, "and may be vulnerable.")

# Port # <function portscanner at 0x0000016876D881F0> is open and may be vulnerable.