# Microbit Lesson 1: Getting started

## Lesson overview

This lesson:

* Introducing the Microbit, Mu & Python
* Running your first program on the Microbit
* Basic syntax of Python
* Debugging tips

## Video

* [Microbit lesson 1 video](https://youtu.be/BPgkJJkEu_k)

## Introducing

![](img/microbit-hardware.png)

The Microbit

* Small board that can be easily programmed. Contains 5x5 grid of LEDs, 2 buttons, acceleromter, compass, touch sensors, temperature sensor, bluetooth radio

Python

* Popular and versitile programming language that is quite easy to learn.

Mu Editor

* The software on your laptop we will use. Look for **mu Editor** in your programs menu. Set mode to **BBC micro:bit** when prompted.

## Connecting your Microbit

![](img/microbit-usb.jpg)

## Your first program

```python
from microbit import *

# Display 'Hello world!' then the happy emoji
display.scroll("Hello world!")
display.show(Image.HAPPY)
```

(Demo)

## Syntax of your first program

Features of your first program

* Statements are executed in order, top down - unless otherwise directed
* Importance of casing, consistent spelling and correct symbols
* The import statement - every microbit program will need this. Loads the Microbit functionality. Python has "core" functionality available to every program. If we want to use something not available by default, we can use import statements to tell Python to load it.
* Comments -  every program should include comments.
* Scroll text - note the parenthesis and quote marks
* Images - there is quite a list available

## Tips for correcting your programs (debugging)

* Run your code everytime you make a change.
* Read the error message.
* Google the error message.
* Guess and check - really it's ok to have a guess!
* Comment out code.
* Ask a peer for help - learn from each other!
* Ask the teacher.

When asking for help...

* Explain what you’re trying to do.
* Show the code that’s giving the error.
* Show the entire stack trace including the error message.
* Explain 2-3 things that you’ve tried already and why they didn’t work.

## Activity: Quick familiarity

Spend a few minutes experimenting with different messages and the built in emoji images.

When ready, try using the following additional commands:

```python
# Will pause the program for 1000 milliseconds
sleep(1000)                 

# Clear the entire LED grid
display.clear()             

# Set pixel 3rd column, 5th row to brightness 9 (full)
display.set_pixel(2,4,9)    

# To create your own image, setting each LED individually
# -- 0 indicates off, 9 indicates on (full brightness)
display.show(Image("09090:99999:09090:99999:09090"))
```

## Activity: Create an animated art piece

With time remaining create an animated art piece on the microbit. 

You can use any mix of the commands shown so far.

For example:

* Stick person moving across screen
* Stick person jumping and landing
* However your creativity inspires...?


