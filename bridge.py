import socket
from os import environ

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 8000))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect((environ["SERVER_IP"], 8000))

connection = client_socket.makefile('wb')

print(f"Started Bridge at 0.0.0.0:8000 to {environ['SERVER_IP']}:8000")
while True:
    data = server_socket.recv(131072)
    print(f"Received {len(data)} bytes: {data.hex()}")
    if not data:
        break
    connection.write(data)
