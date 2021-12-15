# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal
#
# WiPy WiFi setup, augmented code from:
# http://micropython.org/resources/docs/en/latest/wipy/wipy/tutorial/wlan.html#assigning-a-static-ip-address-when-booting

import machine
from network import WLAN

IP = '192.168.1.4'
SUBNET = '255.255.255.0'
GATEWAY = '192.168.1.254'
DNS_SERVER = '8.8.8.8'
SSID = 'ssid_here'
WIFI_PASS = 'password_here'

wlan = WLAN()

if machine.reset_cause() != machine.SOFT_RESET:
    wlan.init(WLAN.STA)
    wlan.ifconfig(config=(IP, SUBNET, GATEWAY, DNS_SERVER))

if not wlan.isconnected():
    wlan.connect(SSID, auth=(WLAN.WPA2, WIFI_PASS), timeout=5000)

    while not wlan.isconnected():
        machine.idle()  # save power while waiting

