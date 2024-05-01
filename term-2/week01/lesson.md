# PWM

Begin with this code sample, and an LED (with resistor) on Pin 0, and just let them play with it to try and figure out what the new parts of the code they haven't seen before do.

```py
from machine import *
import time

led_pwm = PWM(Pin(0))
led_pwm.freq(100)
led_pwm.duty_u16(32768)
```

What is special about '32768'? How might this relate to `u16`? (the answers are: 32768 is 2^15, and is half of the largest number represented in 16 bits (65535)).

Try setting the duty to 0 and to 65535, and see how this changes the brightness of the LED.

What is 'frequency' and how does it relate to duty and the LED's brightness?