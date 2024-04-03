from machine import Pin
import time
button = Pin(0,Pin.IN, Pin.PULL_UP)
led = Pin(1,Pin.OUT)
previous = button.value()
while True:
    buttonStatus = button.value()
    if buttonStatus == 0 and previous == 1:
        led.toggle()
    previous = buttonStatus


