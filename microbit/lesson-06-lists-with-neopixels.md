# Microbit Lesson 6: Lists with Neopixels

## Video

* [Microbit lesson 6 video](https://youtu.be/c1RAGaOKYNo)

## Sample program

```python
from microbit import *
from neopixel import NeoPixel
leds = NeoPixel(pin1, 8)

# Define my colours
white =     [255, 255, 255]
blue =      [  0,   0, 255]
red =       [255,   0,   0]
green =     [  0, 255,   0]
magenta =   [255,   0, 255]
black =     [  0,   0,   0]

# Define a function to set all LEDs to black
def clear_leds():
    number = 0
    while number < 8
        leds[number] = black
        number = number + 1
    leds.show()

# Make green and magenta opposing chasers
clear_leds()
number = 0
while True:
    clear_leds()
    leds[number] = green
    leds[7-number] = magenta
    number = number + 1
    if number == 8:
        number = 0
```
