# set up a mini server where multiple clients may communicate 
import socket
import threading 

hostName = '192.168.1.1' # localhost
port = 55555 # any port you want that's not too popular or know, should be tcp.

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((hostName, port)) # connect the host to port 55555 
server.listen()


clients = []
nicknames = []

def messager(message): 
    for client in clients:
        client.send(message)

def handler(client):
    while True: 
        try: 
            message = client.recv(1024) # 1024 bytes of info 
            messager(message) 
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            messager(f'{nickname} has left the chatroom.'.encode('ascii'))
            nicknames.remove(nickname)
            break
# if client leaves, alert the rest of the clients that the person has left the chatroom.     
    
def receive():
    while True:
        client, address = server.accept() # accept all clients
    print(f'Connected via {str(address)}') # if client connects, give their IP address

    client.send('NAME'.encode('ascii')) # send codeword NAME to person
    nickname  = client.recv(1024).decode('ascii') # decode to client 
    nicknames.append(nickname) # print it to the list 
    clients.append(client) # execute 

    print(f'The connected clients name is {nickname}.. Sup') # give alertion that the person has joined 
    messager(f'{nickname} has joined the chatroom, welcome.'.encode('ascii')) # connection success
    client.send('Connected to the server, hi.'.encode('ascii')) # implies that you're in the server.

    thread = threading.Thread(target=handler, args=(client,))
    thread.start()

print("Chat has now started...")    

receive()


# backend code, welcomes / leaves, etc 

# keep getting "Traceback (most recent call last):
#  File "C:\Users\ryana\OneDrive\Desktop\NTWRKING\TCPCHATSERVER.py", line 9, in <module>
#    server.bind((hostName, port)) # connect the host to port 55555
# SError: [WinError 10049] The requested address is not valid in its context"