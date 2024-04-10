from machine import Pin
import time
import random

led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)
led3 = Pin(2, Pin.OUT)

leds = [led1, led2, led3]

btn1 = Pin(3, Pin.IN, Pin.PULL_UP)
btn2 = Pin(4, Pin.IN, Pin.PULL_UP)
btn3 = Pin(5, Pin.IN, Pin.PULL_UP)

btns = [btn1, btn2, btn3]

pattern = []

for led in leds:
    led.off()

while True:
        
    nextValue = random.getrandbits(16)%3
    pattern.append(nextValue)
    
    for position in pattern:
        leds[position].on()
        time.sleep(0.5)
        leds[position].off()
        time.sleep(0.2)
        
    patternCorrect = True
    
    for position in pattern:
        
        while btn1.value() == 1 and btn2.value() == 1 and btn3.value() == 1:
            pass
        if btn1.value() == 0 and position == 0:
            pass
        elif btn2.value() == 0 and position == 1:
            pass
        elif btn3.value() == 0 and position == 2:
            pass
        else:
            while True:
                led1.on()
                led2.on()
                led3.on()
        
        while btn1.value() == 0 or btn2.value() == 0 or btn3.value() == 0:
            pass
        time.sleep(0.1)
        
    time.sleep(1)
