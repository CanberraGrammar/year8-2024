from machine import Pin
import time
led = Pin(0, Pin.OUT)
led.toggle()
led2 = Pin(1, Pin.OUT)
led2.toggle()

