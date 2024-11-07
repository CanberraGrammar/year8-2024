import time
import requests
import json
import network

ssid = 'CC-Y8'
password = 'raspberrypi'

wlan = network.WLAN(network.STA_IF) 
wlan.active(True)
wlan.connect(ssid, password) 
while wlan.isconnected() == False: 
    print('Waiting for connection...') 
    sleep(1) 
ip = wlan.ifconfig()[0]

print(f'Connected on {ip}')

url = 'http://example.com'

data = requests.get(url)
print(data.text)