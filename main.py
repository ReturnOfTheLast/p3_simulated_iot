import socket
from time import sleep
import random
import network

"""This will act as an lifx LED-light IoT device"""

SSID = "threefivezero_iot"
PASSWORD = "ALongAndComplicatedPassword"
HOST = "10.10.0.223"
BUFFER_SIZE = 1024
PORT = 12345

with open("names-dataset.txt", "r") as fd:
    lines = [x.strip() for x in fd.readlines()]

# Connect to WLAN (Router WIFI)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.ifconfig(("10.10.0.5", "255.255.255.0", "10.10.0.1", "1.1.1.1"))
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    print("Waiting for connection...")
    sleep(1)

# TCP Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    data = random.choice(lines)
    client_socket.send(data.encode())
    print(f"Data send: {data}")
    sleep(2)  # Skal slettes efter Pico W testes eksternt
