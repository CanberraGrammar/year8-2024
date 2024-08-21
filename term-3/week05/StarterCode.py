import network 
import socket 
from time import sleep 
from machine import * 
 
ssid,password = open("wifi.txt").read().split(",") 
 
#Connect to WLAN 
wlan = network.WLAN(network.STA_IF) 
wlan.active(True) 
wlan.connect(ssid, password) 
while wlan.isconnected() == False: 
    print('Waiting for connection...') 
    sleep(1) 
ip = wlan.ifconfig()[0]
print(f'Connected on {ip}')
address = (ip, 80)
connection = socket.socket()
connection.bind(address)
connection.listen(1)