from machine import *
import time

joyX = ADC(Pin(26))
joyY = ADC(Pin(27))
joyBtn = Pin(16,Pin.IN,Pin.PULL_UP)

while True:
    readingX = joyX.read_u16()/32768-1
    readingY = joyY.read_u16()/32768-1
    print(readingX, readingY)
    time.sleep_ms(10)
