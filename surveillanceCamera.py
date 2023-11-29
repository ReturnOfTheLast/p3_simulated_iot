import socket
import time
import picamera
from os import environ

<<<<<<< HEAD
# Connect a client socket to my_server:8000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect((environ["SERVER_IP"], 8000))
=======

HOST = "10.0.0.35"
PORT = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
client_socket.connect((environ[HOST], PORT))
>>>>>>> 53aa9d13ed33190fc1e1848e3e3e15530316122d

# Make a file-like object out of the connection
connection = client_socket.makefile('wb')
try:
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        camera.framerate = 24
        camera.rotation = 180

        # Start a preview and let the camera warm up for 2 seconds (necessary)
        camera.start_preview()
        time.sleep(2)

        # Start recording, sending the output to the connection for 60
        # Seconds, then stop
        camera.start_recording(connection, format='h264')
        print("Started recording")

        # 'while loop' used to keep the camera recording
        while True:
            pass
finally:
    connection.close()
    client_socket.close()
