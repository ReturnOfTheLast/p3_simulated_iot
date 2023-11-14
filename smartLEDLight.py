import time
import random
import network
import urequests


"""This will act as an Smart LED-light IoT device"""

SSID = "threefivezero_iot"
PASSWORD = "ALongAndComplicatedPassword"
HOST = "10.10.0.223"
PORT = 12345

# Connect to WLAN (Router WIFI)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.ifconfig(("10.10.0.5", "255.255.255.0", "10.10.0.1", "1.1.1.1"))
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    print("Waiting for connection...")
    time.sleep(1)

i = 0

while True:
    data = {"state": i}
    i = (i + 1) % 2
    r = urequests.post(f"http://{HOST}:{PORT}/api/v2/lightstatus", json=data)
    print(r.status_code)
    print(r.json())

    # Delay for each packet bewteen 0 - 2 sec
    time.sleep(round(random.random() * 2, ndigits=2))
