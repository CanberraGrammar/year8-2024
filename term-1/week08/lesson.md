# Term 1 Session 3 (Week 8)

## Introduction to circuits

We start with a quick demonstration of holding the motor wires onto the 9V battery, and showcasing that the electrons flow both ways and hence the motor will work either way. Now we do the same with an LED and show 'oh, it doesn't work both ways'.

This only works one way, when the positive end of the battery is connected to the longer led of the LED. How can we do this without manually holding it onto a battery?

Enter the Raspberry Pi Pico! We have GPIO pins that can provide a high/low voltage, and ground pins.

## How to wire up an LED

We need to choose a GPIO pin to attach the LED to. We will use GPIO 0 and GPIO 1 (see pinout diagram).

Attach a wire to GPIO 0, and plug it into one of the standard breadboard rows (e.g. row 30).
Plug the LED's longer leg into row 30 as well, so it is connected to the wire.
Plug the resistor into the same row as the shorter leg of the LED (so row 31 or 29), and put the other leg of the resistor in any other row.
Connect the other leg of the resistor to a GND pin (square) with another wire.

We can now interact with that LED via code!

```python
from machine import Pin
import time
led = Pin(0, Pin.OUT)

led.on()
time.sleep(1)
led.off()
time.sleep(1)
led.toggle()
```

Adding another LED to GPIO 1 follows the same pattern - and to prevent issues with groundingn / insufficient power / etc, placing everything on its own closed circuit loop (so no sharing of resistors/grounds) is the easiest solution.

## Activities

### Blinky

Make LEDs blink on and off in a pattern that you like :) you may need `time.sleep` - don't forget you can sleep for fractional amounts too! (`time.sleep(0.5)` for instance).

### Traffic Lights

When the program starts running, turn on the red light, wait five seconds, then turn on the green light for five seconds, then yellow for two, then red again, and leave it at red. (like normal traffic lights, only one is on at any time).

```python
from machine import Pin
import time
ledRed = Pin(0, Pin.OUT)
ledYellow = Pin(1, Pin.OUT)
ledGreen = Pin(2, Pin.OUT)

ledRed.on()
ledYellow.off()
ledGreen.off()

time.sleep(5)

ledRed.off()
ledGreen.on()

time.sleep(5)

ledGreen.off()
ledYellow.on()

time.sleep(2)

ledYellow.off()
ledRed.on()
```

### FizzBuzz / FizzBlink

Make the classic FizzBuzz game, printing out one number per second, except blink one LED for Fizz, another for Buzz, and both for FizzBuzz:

```python
from machine import Pin
import time
ledFizz = Pin(0, Pin.OUT)
ledBuzz = Pin(1, Pin.OUT)

ledFizz.off()
ledBuzz.off()

for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    ledFizz.on()
    ledBuzz.on()
  elif i % 3 == 0:
    ledFizz.on()
  elif i % 5 == 0:
    ledBuzz.on()

  print("i")
  time.sleep(1)
  ledFizz.off()
  ledBuzz.off()
```

If you get to this stage, you could a third LED to the FizzBlink demo above, and make it work for three numbers (e.g. `3, 5, 7`).
