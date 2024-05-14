from machine import *
import time
 
led_pwm = PWM(Pin(0)) 
led_pwm.freq(100)

btn = Pin(1,Pin.IN,Pin.PULL_UP)

while True:
    for duty in range(0,65535):
        led_pwm.duty_u16(duty)
        if btn.value() == 0:
            print(duty)
            while btn.value() == 0:
                pass
        #Here
    
    for duty in range(65535,0,-1):
        led_pwm.duty_u16(duty)
        if btn.value() == 0:
            print(duty)
            while btn.value() == 0:
                pass
        #Here





