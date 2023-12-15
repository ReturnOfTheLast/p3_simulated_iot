import socket

HOST = "10.10.0.108"
PORT = 8000

#Create UDP Server using IPv4
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Bind socket to host and port
server_socket.bind((HOST,PORT))

print("UDP server listening for incoming messages")

#Receive data from surveillance camera (IoT)
while True:
    data, addr = server_socket.recvfrom(65535)
    print(f"Received {len(data)} bytes from {addr}")
