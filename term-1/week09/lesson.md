# Term 1 Session 4 (Week 9)

## Introduction to buttons

Demonstrate how to connect the button to the breadboard. Wire it up complete with an LED and resistor to the VBUS signal (5th pin down on the right).

The result should be a button that turns on and off the LED in hardware (with no code). 

### Adding code interaction

Plug in the button on one end to GP Pin 0, and the other side into ground. Then add this code to Thonny:

```python
from machine import Pin
import time
button = Pin(0, Pin.IN, Pin.PULL_UP)
print(button.value())
```

Then, if you run this code while the button is not pressed, the output should be `1`. If you run this code while the button is pressed, the output should be `1`.  
(the reason this is inverted from what one might exepect is because the `PULL_UP` specifier says 'treat GROUND as high state, and non-ground as low voltage')

To print out the status of the button continuously, we can replace the single `print` line with:

```python
while True:
    print(button.value())
    time.sleep(0.01) # This is needed to avoid flooding the buffer and not seeing updates
```

## Activities

### Controlling an LED through software

Connect the LED and resistor on its own loop on GP 1, and the button on GP 0 (as detailed above). Then connect them via code to make the button change the LED's state (on when pressed, off when not).

Using the above wiring, the code would look like:

```python
from machine import Pin
import time
button = Pin(0, Pin.IN, Pin.PULL_UP)
led = Pin(1, Pin.OUT)

while True:
    time.sleep(0.01)
    if button.value() == 0:
        led.on()
    else:
        led.off()
```

### Using a button as a toggle switch

```python
from machine import Pin
import time
button = Pin(0, Pin.IN, Pin.PULL_UP)
led = Pin(1, Pin.OUT)
previous = button.value()

while True:
    buttonState = button.value()
    if buttonState == 0 and previous == 1:
        led.toggle()
    previous = buttonState
```
