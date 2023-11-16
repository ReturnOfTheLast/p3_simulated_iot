import time
import network
import random
import math
import urequests

"""This will act as an Smart Watch IoT device"""

SSID = "threefivezero_iot"
PASSWORD = "ALongAndComplicatedPassword"
HOST = "10.0.0.35"
PORT = 5000

# Connect to WLAN (Router WIFI)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.ifconfig(("10.10.0.5", "255.0.0.0", "10.10.0.1", "1.1.1.1"))
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    print("Waiting for connection...")
    time.sleep(1)

# https://forbes.com/health/healthy-aging/normal-heart-rate-by-age/ (heartrate:
# sqrt((162 - 95) / 2)) = 5.79


def generate_normal_distribution(mu, sigma):
    # Box-Muller transform func:
    x1 = 1.0 - random.uniform(0, 1)
    x2 = 1.0 - random.uniform(0, 1)
    eq = math.sqrt(-2.0 * math.log(x1)) * math.cos(2 * math.pi * x2)

    result = mu + eq * sigma
    return result


mu = 128.5
sigma = 5.79

while True:
    data_bpm = round(generate_normal_distribution(mu, sigma), 2)
    timestamp = time.time()
    data = [data_bpm, timestamp]

    r = urequests.post(f"http://{HOST}:{PORT}/api/v2/smartwatch",
                       json=data)
    print(r.status_code)
    print(r.json())

    data = []
    # Delay for each packet bewteen 0 - 3 sec
    time.sleep(round(random.random() * 3, 2))
