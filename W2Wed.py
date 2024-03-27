from machine import Pin
import time
led = Pin(25, Pin.OUT)
count = int(input("How big? "))
for i in range(count):
    print("* "*(i+1))