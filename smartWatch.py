import time
import network
import socket

SSID = "threefivezero_iot"
PASSWORD = "ALongAndComplicatedPassword"
HOST = "xxx"
BUFFER_SIZE = 1024
PORT = 12345

# Connect to WLAN (Router WIFI)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.ifconfig(("xxx", "xxx", "xxx", "xxx"))
wlan.connect(SSID, PASSWORD)


# TODO:
# Send timestamp and heartbeat (BPM)
# Setup socket (TCP)
# Setup network
# Make a function for how heartbeat BPM will be emulated
