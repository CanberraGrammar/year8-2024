from machine import *
from ssd1306 import SSD1306_I2C
import time

#i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
#oled = SSD1306_I2C(128, 64, i2c)

potX = ADC(Pin(26))
potY = ADC(Pin(27))

while True:
    print(potX.read_u16(),potY.read_u16())
    time.sleep(0.01)