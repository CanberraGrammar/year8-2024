from machine import *
from ssd1306 import SSD1306_I2C
import time

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

potX = ADC(Pin(26))
potY = ADC(Pin(27))

btn = Pin(2,Pin.IN,Pin.PULL_UP)

lines = []

x = int((potX.read_u16() / 65535) * 128)
y = int((potY.read_u16() / 65535) * 64)

while True:
    px = x
    py = y
    x = int((potX.read_u16() / 65535) * 128)
    y = int((potY.read_u16() / 65535) * 64)
    print(x,y)
    oled.fill(0)
    if btn.value() == 1:
        lines.append((x,y,px,py))
        
    for line in lines:
        startX, startY, endX, endY = line
        oled.line(startX, startY, endX, endY, 1)
    oled.pixel(x-1,y,1-oled.pixel(x-1,y))
    oled.pixel(x+1,y,1-oled.pixel(x+1,y))
    oled.pixel(x,y-1,1-oled.pixel(x,y-1))
    oled.pixel(x,y+1,1-oled.pixel(x,y+1))
    oled.show()
    time.sleep(0.01)
    
