import socket
import select
import sys


client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 4426
client_socket.connect(('127.0.0.1', port))

while(True):
    message = input("enter your message:")
    client_socket.sendall(message.encode('encrypted-0598'))

    if (message == 'CLOSE SOCKET'):
        client_socket.close()
        break

    response = client_socket.recv(1024).decode('encrypted-0598')

    print('server:', response)




