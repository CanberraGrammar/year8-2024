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

for led in leds:
    led.off()

pattern = []
while True:
    pattern.append(random.choice([0,1,2]))
    
    # Diplaying LEDS
    for item in pattern:
        leds[item].on()
        time.sleep(0.5)
        leds[item].off()
        time.sleep(0.2)
    
    
    # Read Buttons
    for item in pattern:
        buttonPressed = False
        while not buttonPressed:
            #Check if a button is pressed
            for btn in btns:
                if btn.value() == 0:
                    buttonPressed = True
        
        if btns[item].value() == 1: #Not Pressed
            while True:
                for led in leds:
                    led.on()
                    
        #Wait until all buttons are released
        while buttonPressed:
            buttonPressed = False
            for btn in btns:
                if btn.value() == 0:
                    buttonPressed = True
        
        time.sleep(0.1)
    time.sleep(0.5)







