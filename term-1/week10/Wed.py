from machine import Pin
import time
import random

led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)
led3 = Pin(2, Pin.OUT)

btn1 = Pin(3, Pin.IN, Pin.PULL_UP)
btn2 = Pin(4, Pin.IN, Pin.PULL_UP)
btn3 = Pin(5, Pin.IN, Pin.PULL_UP)