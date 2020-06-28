# Variables & numbers

* Video: [Learning Python (2018 edition) 01: Your first programs](https://www.youtube.com/watch?v=dOCTDDxtv7s) (Variables, numbers, strings & casting)

## Basic calculations

Python supports all the basic arithmetic calculations

```python
print( 2 + 2 )
print( 1.5 + 2.25 )
print( 7 - 2 )
print( 3 * 4 )
print( 10 / 2 )
print( 4 ** 3 )    # Exponent operator
```

A note about division & modulus

```python
print( 13 / 5 )   # Real number divison
print( 13 // 5 )  # Integer divison
print( 13 % 5 )   # Modulus
```

## Variables

Variables are just a named memory location

Defining a variable in Python is as simple as assigning a value to a name. 

```python
a = 10
```

* Names must start with an alpha character or underscore, but may then contain numeric characters.
* Names should be meaningful. Establish good habbits early. It should be obvious from the name of the variable what it's purpose is.
* Python's preferred practice is to separate_words_with_underscores rather than using camelCase like otherLanguages. 
* Be warned variable names are case sensitive. `Variable` is not the same as `variable`.

```python
var = 10
print(Var) # Will not work!
```

## Using variables in calculations

Calculations can be assigned on a right goes into left basis.

```python
val = 5 + 3
print(val)
```

Variables can be used as part of a calculation as well

```python
a = 5 + 3
b = a * 4
c = a - b
print( c ** a )
```

## Integers vs real numbers

It is possible to denote the value of a variable to be a real number simply by adding a decimal element.

```python
print(type(13))
print(type(13.0))
```

To convert a real number to integer, use the `int()` command to truncate, or `round()` to round.

```python
a = 13.6
b = int(a)
c = round(a)
print(a,b,c)
```

To convert an integer to real, use the `float()` command.

```python
a = 13
b = float(a)
print(a,b)
```

## Other numerical functions

```python
import math
answer = math.pi                # π = 3.141592
answer = math.e                 # the natural number, e = 2.718281
answer = math.sqrt(100)         # Square root
answer = math.gcd(104,64)       # Greatest common divisor
answer = math.log(1024,2)       # Log of base 2
answer = math.hypot(6,8)        # Hypothenus of triangle with sides 6, 8
answer = math.cos( angle )      # Cosine of angle (radians)
answer = math.sin( angle )      # Sine of angle (radians)
answer = math.tan( angle )      # Tangent of angle (radians)
answer = math.acos( adj/hypot ) # Arc-cosine in radians
answer = math.asin( opp/hypot ) # Arc-sine in radians
answer = math.atan( opp/adj )   # Arc-tan in radians
answer = math.degrees( rad )    # Convert radians to degrees
answer = math.radians( deg )    # Convert degrees to radians
answer = abs( val )             # Absolute value

import random
num = random.randint(0,100)     # Random number between 0 and 99 inclusive
```

## Problem set

The following questions assume you will use variables as the inputs into the problem, so the problems can re-caclulate solutions by changing the value assigned to the variable. You should also print the given information in your answer.

1. For any given number, extract the 10s digit. For example, `The tens digit in 1234 is 3.`
2. Area of a right angled triangle calculator. Given values for `base` and `height`, print the area.
3. For any two digit number, swap the position of the digits. For instance, `79` becomes `97`.
4. For any three digit number, print the sum of the three digits. For instance `273` becomes `12` (2+7+3)
5. For any given year, print the century that year belongs to. Remember that 1999 and 2000 were the 20th century, whereas 2001 was the beginning of the 21st century.
6. Given a number representing the number of seconds since midnight, print the time in 24hour clock format. For example `70500` seconds should print a time of `19:35`.
7. Area of a non-right angled triangle calculator. Given values for length `a`, length `b` and angle in degrees `C`, return the area of the triangle (remember you will have to convert degrees to radians first).
8. For any given values for `a`, `b` and `c`, will provide the solutions to the quadratic formula (you may assume both solutions are required). Be careful with your order of precedence. Here is an example solution set for testing: If `y=2x^2-4x-10` then the solutions are `3.44949` and `-1.44949`.
