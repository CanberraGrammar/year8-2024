import network 
import socket 
from time import sleep 
from machine import * 

ssid = "CC-Y8"
password = "raspberrypi"

colours = ["red", "yellow", "green"]
leds = []

i = 0
while i < len(colours):
    leds.append(Pin(i,Pin.OUT))
    i = i + 1

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

    for i in range(len(leds)):
        colour = colours[i]
        if path == "/"+colour+"on?":
            leds[i].on()
        elif path == "/"+colour+"off?":
            leds[i].off()
                
    html = '''<html>
      <head>
      </head>
      <body>'''
    
    for i in range(len(colours)):
        colour = colours[i]
        if leds[i].value() == 1:
            html = html + '<form method="get" action="/'+colour+'off">'
            html = html + '<label>'+colour+' LED is on</label>'
            html = html + '<input type="submit" value="Turn '+colour+' LED off">'
            html = html + '</form>'
        else:
            html = html + '<form method="get" action="/'+colour+'on">'
            html = html + '<label>'+colour+' LED is off</label>'
            html = html + '<input type="submit" value="Turn '+colour+' LED on">'
            html = html + '</form>'
    
    html = html + '''
      </body>
    </html>'''
    
    client.send(html)
    client.close()

