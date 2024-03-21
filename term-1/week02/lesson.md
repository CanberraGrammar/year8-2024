# Code Cadets Year 8 Term 1 Week 2

## Blinky

How to use the `sleep` function from the `time` module:

```py
import time

time.sleep(1)
```

### Your task

Write a program which will toggle the onboard LED once per second, forever.

### Starting code

```py
from machine import Pin
import time

led = Pin(25, Pin.OUT)

# To toggle the LED once
led.toggle()

# To pause for a second
time.sleep(1)
```

## Lightshow

### Your task

Spend ~10 minutes with these functions to create the best lightshow you can! :)

### Starting code

```py
from machine import Pin
import time

led = Pin(25, Pin.OUT)

# To toggle the LED once
led.toggle()

# To pause for a second
time.sleep(1)
```
