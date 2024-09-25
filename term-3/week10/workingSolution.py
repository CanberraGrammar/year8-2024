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

images = []

while True:
    client = connection.accept()[0]
    request = str(client.recv(1024))
    path = request.split()[1]
    print(path)
    path = path[6:]
    print(path)
    
    if path == ("circle"):
        oled.ellipse(10, 10, 10, 10, 1)
        images.append("circle")
    elif path == ("square"):
        oled.rect(5, 5, 20, 20, 1)
        images.append("square")
    elif path == ("vline"):
        oled.vline(8, 8, 5, 1)
        images.append("vline")
    elif path == ("hline"):
        oled.hline(8, 8, 5, 1)
        images.append("hline")
    elif path == ("clear"):
        oled.fill(0)
        images.clear()
    elif path == ("undo"):
        images.pop()
        oled.fill(0)
        for image in images:
            print("image: " + image)
            if image == "circle":
                oled.ellipse(5, 5, 5, 5, 1)
            elif image == "square":
                oled.rect(5, 5, 5, 5, 1)
            elif image == "vline":
                oled.vline(5, 5, 5, 1)
            elif image == "hline":
                oled.hline(5, 5, 5, 1)
            
    oled.show()

    html = open("pictures.html").read()

    client.send(html)
    client.close()
