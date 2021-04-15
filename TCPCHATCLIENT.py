import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.1', 55555))  # default gateway binded to port 55555


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
            except:
                print("ERROR. TRY AGAIN.")
                client.close()
                break

      
def write(): 
    while True: 
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))
    
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)



            # the chooses a nickname to connect to the server and allows you to talk

# error atm -- keep getting "invalid syntax (<unknown>, line 15) although i cannot seem to find an error lol

