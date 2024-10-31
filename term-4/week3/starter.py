import network 
import socket 
from time import sleep 
from machine import *
from ssd1306 import SSD1306_I2C
 
ssid = "CC-Y8"
password = "raspberrypi"

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
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
connection.bind(address)
connection.listen(1)

while True:
    client = connection.accept()[0]
    request = str(client.recv(1024))
    if len(request.split()) > 2:
        path = request.split()[1]
        
    html = open("drive.html").read()
    
    client.send(html)
    client.close()


