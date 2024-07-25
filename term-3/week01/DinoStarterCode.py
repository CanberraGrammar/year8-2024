from machine import *
from ssd1306 import SSD1306_I2C
from random import *
import time
import math
 
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
 
btnJump = Pin(2, Pin.IN, Pin.PULL_UP)
btnDuck = Pin(3, Pin.IN, Pin.PULL_UP)
 
floorY = 48.0
 
dinoX = 16
dinoY = floorY
dinoVY = 0
dinoAY = 0.15
dinoWidth = 8
dinoHeight = 16

obstacles = []

while True:
 
    obstacles = [(74,40,8),(128,24,15)]
 
    gameRunning = True
 
    score = 0
 
    isDucking = False
 
    while gameRunning:
 
        starttime = time.ticks_ms()
        oled.fill(0)
 
        # Call functions for the game here
 
        oled.show()    
        endtime = time.ticks_ms()
        time.sleep_ms(30 - (endtime - starttime))
 
    oled.fill(0)
    oled.text("Game Over",28,28,1)
    oled.text("Score: " + str(score),64-len("Score: " + str(score))*4,36)
    oled.show()
 
    while btnJump.value() == 1 and btnDuck.value() == 1:
        time.sleep_ms(10)