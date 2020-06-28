# Microbit Lesson 3: Numeric operations

## Lesson overview

This lesson:

* Assigning variables (right goes into left)
* Generating random numbers
* Operators for calculation

## Video

* [Microbit lesson 3 video](https://youtu.be/jivYnqzNIXA)

## What is a variable?

A named location in the computer’s memory that you can use to store a value to and read values from.

## First example

In this example, we create a named variable `account_balance` and assign it a starting value of `100`. We can then access that value any place where we might have used the number 100 previously, such as in the scroll() command.

```python
from microbit import *

account_balance = 100
display.scroll( account_balance )
```

One golden rule with assigning variable values in Python is that the name of the target variable we want to place a value in must be on the left side of the equal sign. The value we want to place, or something to calculate a value, must go on the right.

To illustrate this,

```python
from microbit import *

weeks = 3
weekly_allowance = 200
account_balance = weeks * weekly_allowance
display.scroll( account_balance )
```

## Numeric variables and addition

How will the following program change the value of `n` as it runs? What will be output to the display?

```python
from microbit import *

n = 0
while n < 100:
    n = n + 1
    display.scroll(n)
display.scroll("bye")
```

* What will the above do?
* How can we use the buttons to add/subject 1 to the number?

## Arithmetic

We can perform a range of arithmetic operations on variables using the following operators:

* Addition... `+`
* Subtraction... `-`
* Multiplication... `*`
* Division... `/` 

An example using subtraction and multiplication follow...

```python
from microbit import *

n = 0
while n < 100:
    n = n + 1
    if button_a.was_pressed():
        n = n - 10
    if button_b.was_pressed():
        n = n * 2
    display.scroll(n)
```

## Using a random number generator

While learning about numbers, it can be handy for Microbit games to know how to generate a random number. 

Firstly import the `random` library as it is not part of default Python.

```python
from microbit import *
import random
```

Then to ask for a random number between 0 and 99, to be saved into a variable called `num`, the code would look like

```python
num = random.randint(0,99)
```

So we can add this to our previous program...

```python
from microbit import *
import random

n = 0
while n < 100:
    n = n + 1
    if button_a.was_pressed():
        n = n - 10
    if button_b.was_pressed():
        n = n * 2
    if pin0.is_touched():
        n = random.randint(0,99)
    display.scroll(n)
```

## Modulus

Not in the video, but a useful thing for programmers to know about: The modulus. Effectively it is "the remainder" from a divison. For instance, if calculated 14 divided by 5, the answer would be 2 with 4 left over as remainder. In Python we can do this in two steps. To perform the division with the whole number of 5s that would go into 14, it would be `14 // 5` to return `2`, and to find out the remainder that would look like `14 % 5` which would return a value of `4`. 

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
