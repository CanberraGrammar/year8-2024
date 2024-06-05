from machine import *
from ssd1306 import SSD1306_I2C
import time

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

potX = ADC(Pin(26))
potY = ADC(Pin(27))

x = int((potX.read_u16() / 65535) * 128)
y = int((potY.read_u16() / 65535) * 64)

while True:
    px = x
    py = y
    x = int((potX.read_u16() / 65535) * 128)
    y = int((potY.read_u16() / 65535) * 64)
    print(x,y)
    oled.line(x,y,px,py,1)
    oled.show()
    time.sleep(0.01)
    
