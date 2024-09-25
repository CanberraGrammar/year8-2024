import network 
import socket 
from time import sleep 
from machine import *

from machine import I2C
from ssd1306 import *

i2c = machine.I2C(0,sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
oled = SSD1306_I2C(128,64,i2c)

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
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
connection.bind(address)
connection.listen(1)

# list of images drawn
images = []

while True:
    client = connection.accept()[0]
    request = str(client.recv(1024))
    path = request.split()[1]
    print(path)
    
    if path == "/?btn=rectangle":
        # draw a rectangle
        oled.rect(10, 10, 30, 40, 1)
        oled.show()
        images.append("rectangle")
    elif path == "/?btn=triangle":
        # draw a triangle
        for i in range(1, 60):
            oled.hline(10, 4 + i, i, 1)
            oled.show()
        images.append("triangle")
    elif path == "/?btn=parallelogram":
        # draw a parallelogram
        oled.hline(10, 10, 40, 1)
        oled.hline(30, 30, 40, 1)
        oled.line(10, 10, 30, 30, 1)
        oled.line(50, 10, 70, 30, 1)
        oled.show()
        images.append("parallelogram")
    elif path == "/?btn=undo":
        oled.fill(0)
        images.pop()
        for image in images:
            if image == "rectangle":
                oled.rect(10, 10, 30, 40, 1)
            elif image == "triangle":
                for i in range(1, 60):
                    oled.hline(10, 4 + i, i, 1)
            elif image == "parallelogram":
                oled.hline(10, 10, 40, 1)
                oled.hline(30, 30, 40, 1)
                oled.line(10, 10, 30, 30, 1)
                oled.line(50, 10, 70, 30, 1)
            oled.show()
        
    html = open("picture.html").read()

    client.send(html)
    client.close()
