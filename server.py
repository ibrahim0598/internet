
import socket
import select
import sys


server_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 4426
server_socket.bind(('127.0.0.1',port))

server_socket.listen(4426)
print("wait please , server is setting up")

while(True):
    client_socket, client_address = server_socket.accept()
    print('connected with', client_address)
    while(True):
        message = client_socket.recv(1024).decode('encrypted-0598')
        if(not message):
            break
        if( message == 'CLOSE SOCKET' ):
           client_socket.close()
           print('connection closed')
        response = message.upper()
        client_socket.sendall(response.encode('encrypted-0598'))

        print(response)
















    



