import network 
import socket 
from time import sleep 
from machine import *
from ssd1306 import SSD1306_I2C
from servo import Servo
 
ssid = "CC-Y8"
password = "raspberrypi"

speed = Servo(pin_id=0)
steering = Servo(pin_id=1)

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
        if path == "/left?":
            print("LEFT")
            speed.write(120)
            steering.write(40)
        elif path == "/forward?":
            print("FORWARD")
            speed.write(120)
            steering.write(90)
        elif path == "/right?":
            print("RIGHT")
            speed.write(120)
            steering.write(140)
        elif path == "/stop?":
            print("STOP")
            speed.write(90)
            steering.write(90)
        
    html = open("drive.html").read()
    
    client.send(html)
    client.close()


