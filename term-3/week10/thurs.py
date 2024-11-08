import network 
import socket 
from time import sleep 
from machine import *
from ssd1306 import SSD1306_I2C

ssid = "CC-Y8"
password = "raspberrypi"

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

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
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
connection.bind(address)
connection.listen(1)

while True:
    client = connection.accept()[0]
    request = str(client.recv(1024))
    if len(request.split()) >= 2:
        path = request.split()[1]
        
        split = path[2:].split("&")
        if len(split) >= 4:
            x = int(split[0].split("=")[1])
            y = int(split[1].split("=")[1])
            width = int(split[2].split("=")[1])
            height = int(split[3].split("=")[1])
            
            oled.fill_rect(x,y,width,height,1)
            oled.show()
            
    html = open("draw.html").read()
    client.send(html)
    client.close()


