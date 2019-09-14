# Microbit Lesson 2: Conditional execution

## Lesson overview

This lesson:

* The idea of conditional execution
* Syntax: The colon and indentation
* if statement
* while statement
* Microbit feature: Buttons
* Microbit feature: Touch pins

## Video

* [Microbit lesson 2 video](https://youtu.be/CQKTHavIYLg)

## Conditional execution: If

Recall last lession we said: *statements are executed in order, top down - unless otherwise directed
*. We will now look at the "unless otherwise directed" bit. 

An `if` statement asks a question. If the answer is `True`, it will run the intended section that immediately follows. Stop intending to return to normal.

```python
from microbit import *

display.scroll("How awesome is Python?")
if button_a.was_pressed():
    display.show(Image.HAPPY)
if button_b.was_pressed():
    display.show(Image.SAD)
```

* What happens if you don't press either button?
* What happens if you press both buttons?

## Conditional execution: While

Consider this one change...

```python
from microbit import *

while True:
    display.scroll("How awesome is Python?")
    if button_a.was_pressed():
        display.show(Image.HAPPY)
    if button_b.was_pressed():
        display.show(Image.SAD)
```

## Nested if's

We can put "if" statements inside other "if" statements. Consider how this would behave?

```python
from microbit import *

display.scroll("Whose your Marvel character?")
display.scroll("Goodie or badie?")
if button_a.was_pressed():
    display.scroll("Boy or girl?")
    if button_a.was_pressed():
        display.scroll("Iron man")
    elif button_b.was_pressed():
        display.scroll("Captain Marvel")
elif button_b.was_pressed():
    display.scroll("Secretly good?")
    if button_a.was_pressed():
        display.scroll("Nebula")
    elif button_b.was_pressed():
        display.scroll("Thanos")
```

## Activity: 20 questions

By creating a series of yes/no questions using if statements inside of if statements, create a reduced version of a 20 questions game.
