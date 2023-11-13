import socket
import time
import random
import network

"""This will act as an Smart LED-light IoT device"""

# TODO:
# 'Turn off / On' function
# Send data through TCP
# Remove data set!
# Timestamp

SSID = "threefivezero_iot"
PASSWORD = "ALongAndComplicatedPassword"
HOST = "10.10.0.223"
BUFFER_SIZE = 1024
PORT = 12345
lightSwitch = ["Light: On", "Light: Off"]

# Connect to WLAN (Router WIFI)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.ifconfig(("10.10.0.5", "255.255.255.0", "10.10.0.1", "1.1.1.1"))
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    print("Waiting for connection...")
    time.sleep(1)

# TCP Socket (client)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    data = random.choice(lightSwitch)
    client_socket.send(data.encode())
    print(f"Data send: {data}")
    # Skal slettes efter Pico W testes eksternt
    time.sleep(round(random.choice(0, 2), 2)) 
