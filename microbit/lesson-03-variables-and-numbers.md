# Microbit Lesson 3: Numeric operations

## Lesson overview

This lesson:

* Assigning variables (right goes into left)
* Generating random numbers
* Operators for calculation

## Video

* [Microbit lesson 3 video](https://youtu.be/Qk8vsXe7Uj4)

## What is a variable?

A named location in the computer’s memory that you can use to store a value to and read values from.

## Numeric variables and addition

```python
from microbit import *

n = 0
while True:
    n = n + 1
    display.scroll(n)
```

* What will the above do?
* How can we use the buttons to add/subject 1 to the number?

## Addition and subtraction

```python
from microbit import *

n = 0
while n < 100:
    n = n + 1
    if button_a.was_pressed():
        n = n + 1
    if button_b.was_pressed():
        n = n - 1
    display.scroll(n)
```

* How can we use pin0 to double the number and pin1 to halve the number?

## Multiplication and division

```python
from microbit import *

n = 0
while n < 100:
    n = n + 1
    if button_a.was_pressed():
        n = n + 1
    if button_b.was_pressed():
        n = n - 1
    if pin0.is_touched():
        n = n * 2
    if pin1.is_touched():
        n = n / 2
    display.scroll(n)
```

## Using a random number generator

Firstly import the `random` library as it is not part of default Python.

```python
import random
```

Then inside your main loop, add...

```python
    if pin2.is_touched():
        n = random.randint(0,99)
```

## Modulus

```python
from microbit import *

n = 0
while True:
    if button_a.was_pressed():
        n = n + 1
    if button_b.was_pressed():
        n = n - 1
    column = n % 5
    row = n // 5
    display.clear()
    display.set_pixel(column, row, 9)
```
