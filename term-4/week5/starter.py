from machine import *
from ssd1306_plus import *
import time
import network
import socket
import json
import sys
import random
import gc

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_PLUS(128, 64, i2c)

joyX = ADC(Pin(26))
joyY = ADC(Pin(27))
joyBtn = Pin(16,Pin.IN,Pin.PULL_UP)

ssid = 'CC-Y8'
wifiPassword = 'raspberrypi'

wlan = network.WLAN(network.STA_IF) 
wlan.active(True)
wlan.connect(ssid, wifiPassword) 
while wlan.isconnected() == False: 
    print('Waiting for connection...') 
    time.sleep(1) 
ip = wlan.ifconfig()[0]

print(f'Connected on {ip}')

def getRequest(ip, path):
    s = socket.socket()
    s.connect((ip , 80))
    s.sendall("GET "+path+" HTTP/1.1\r\n\r\n")
    s.recv(4096)
    response = ""
    res = s.recv(4096).decode()
    while res != "":
        response += res
        res = s.recv(4096).decode()
    return response
    s.close()
    