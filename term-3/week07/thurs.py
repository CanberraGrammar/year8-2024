import network 
import socket 
from time import sleep 
from machine import * 

ssid = "CC-Y8"
password = "raspberrypi"

redLed = Pin(0,Pin.OUT)
yellowLed = Pin(1,Pin.OUT)
greenLed = Pin(2,Pin.OUT)

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
    print(request)
    path = request.split()[1]
    print(path)
    if path == "/redon?":
        redLed.on()
    elif path == "/redoff?":
        redLed.off()
    elif path == "/yellowon?":
        yellowLed.on()
    elif path == "/yellowoff?":
        yellowLed.off()
    elif path == "/greenon?":
        greenLed.on()
    elif path == "/greenoff?":
        greenLed.off()
        
    html = open("led.html").read()
    if redLed.value() == 1:
        html = html.replace("{redStatus}", "on")
        html = html.replace("{redAction}", "off")
    else:
        html = html.replace("{redStatus}", "off")
        html = html.replace("{redAction}", "on")
    
    if yellowLed.value() == 1:
        html = html.replace("{yellowStatus}", "on")
        html = html.replace("{yellowAction}", "off")
    else:
        html = html.replace("{yellowStatus}", "off")
        html = html.replace("{yellowAction}", "on")
        
    if greenLed.value() == 1:
        html = html.replace("{greenStatus}", "on")
        html = html.replace("{greenAction}", "off")
    else:
        html = html.replace("{greenStatus}", "off")
        html = html.replace("{greenAction}", "on")
    
    client.send(html)
    client.close()

