from machine import Pin
import time
button = Pin(0,Pin.IN, Pin.PULL_UP)
led = Pin(1,Pin.OUT)
previous = button.value()
while True:
    currentButton = button.value()
    if currentButton == 0 and previous == 1:
        led.toggle()
    print(button.value())
    time.sleep(0.01)
    previous = currentButton