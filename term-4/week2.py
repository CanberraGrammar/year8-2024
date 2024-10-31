import time
from servo import Servo

speed = Servo(pin_id=0)
steering = Servo(pin_id=1)

speed.write(100)
time.sleep(1)
speed.write(90)