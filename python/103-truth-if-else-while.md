# Truthiness

* Video: [Learning Python (2018 edition) 02: Making decisions](https://www.youtube.com/watch?v=P-LFnqzXUv4) (truth, if, else)

## Boolean variables

* A boolean variable has only two possible values, `True` or `False`
* Booleans are important for selective execution of code.
* Assigning boolean variables

```python
a = True
b = False
print(a,b)
```

## Boolean operations

We can query the values of other variables to determine truth.

```python
result = (10 == 12)     # is equal to
result = (10 > 12)      # greater than
result = (10 >= 12)     # greater than or equal to
result = (10 < 12)      # less than
result = (10 <= 12)     # less than or equal to
result = (10 != 12)     # not equal to
```

We can compound multiple queries together into one statement

```python
result = (10 > 5) and (10 < 100)
result = (10 > 5) or (10 > 50)
result = not (10 > 5) or (10 > 50)
```

Order of precedence: not, and, or (if in doubt, use parenthesis)

## Truth functions for strings

```python
string1 = "Some string"
truth = string1.isnumeric()   # does it contain only numbers?
truth = string1.isalpha()		# does it contain only letters?
truth = string1.islower()		# is it all lowercase?
truth = string1.isupper()		# is it all uppercase?
truth = string1.istitle()		# is it all title case?
truth = string1.isspace()		# is it all spaces?
```

You can also query if a sub string is in a larger string...

```python
exists = "h" in "hello"
exists = "z" in "hello"
```

For example

```python
something = "Hello"
if something.isnumeric():
    val = int(something)
    print("That is a number")
    print(f"It's value is {val}")
elif something.islower():
    print("It is all lowercase")
elif "z" in something:
    print(f"The string '{something}' contains the letter 'z'")
```

# If, elif, else, while

## If

Having determined how to calculate truthfulness, we can use that to conditionally execute statements.

```python
sister_age = 15
brother_age = 12
sister_is_older = sister_age > brother_age
if sister_is_older:
   print("Sister is older")
```

Rather than storing the truthfulness in a boolean variable, you would normally place the query directly in the `if` statement such as:

```python
sister_age = 15
brother_age = 12
if sister_age > brother_age:
   print("Sister is older")
```

* Note the colon and the indentation
* Python will conditionally execute until you return to the previous level of indentation
* This applies whenever a Python line ends with a colon (you'll see it used repeatedly)

## Else

We can also tell Python to run some alternative code if the comparison was not true. That would look like:

```python
sister_age = 15
brother_age = 12
if sister_age > brother_age:
   print("Sister is older")
else:
   print("Brother is older")
```

The example problem has three scenarios. What will the above do if they are twins (same age)?

## Elif

We can link multiple queries together using `elif`. Upon finding the first that resolves to `True`, Python will cease the remaining comparisons.

```python
sister_age = 15
brother_age = 15
if sister_age > brother_age:
   print("Sister is older")
elif: sister_age == brother_age:
   print("Ages are the same! They might be twins!")
else:
   print("Brother is older")
```

## Example

A more detailed example combining several elements.

```python
name_1 = input("Enter person 1's name:")
name_2 = input("Enter person 2's name:")
age_1 = int(input(f"Enter {name_1}'s age:"))
age_2 = int(input(f"Enter {name_2}'s age:"))
diff = abs(age_1 - age_2)
if age_1 > age_2:
   print(f"{name_1} is {diff} years older than {name_2}")
elif age_1 < age_2:
   print(f"{name_2} is {diff} years older than {name_1}")
else:
   print(f"{name_1} and {name_2} are the same age")
```

## Multiple elif's

You can chain as many elif's together as you like.

```python
from datetime import datetime
day_of_week = datetime.now().weekday()
if day_of_week == 0:
    print("Today is Monday")
elif day_of_week == 1:
    print("Today is Tuesday")
elif day_of_week == 2:
    print("Today is Wednesday")
elif day_of_week == 3:
    print("Today is Thursday")
elif day_of_week == 4:
    print("Today is Friday")
elif day_of_week == 5:
    print("Today is Saturday")
elif day_of_week == 6:
    print("Today is Sunday")
```

* (we'll cover how to use date functionality in more detail later)

## While

`while` operates like `if` but will keep looping through the code while the query returns `True`.

```python
val = 0
while val < 10:
    print(f"val is {val}")
    val = val + 1
```

Random number guesser

```python
import random
secret = random.randint(0,100)
guess = int(input("Guess the secret number between 0 and 99:"))
guesses = 1
while guess != secret:
    if guess > secret:
        print("Too high. Try again.")
    else:
        print("Too low. Try again.")
    guess = int(input("Guess the secret number between 0 and 99:"))
    guesses = guesses + 1
print(f"Good job. That took {guesses} guesses.")
```

## Problem set - Truth

What range of inputs is required for each of the following to return True

```python
a = (int)input("Enter a number:")
truthy = 0 < a and 100 > a 
print(truthy)
```

```python
a = (int)input("Enter a number:")
truthy = not 0 < a and 100 > a 
print(truthy)
```

```python
a = (int)input("Enter a number:")
truthy = 0 < a or 100 > a 
print(truthy)
```

```python
a = (int)input("Enter a number:")
truthy = not 0 < a or not 100 > a 
print(truthy)
```

## Problem set - Selection & iteration

1) Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).

2) Suppose you ask the user what the temperature is. Create a program that will respond as follows:

* If the temperature is between 20 and 27, say that it is "Just right"
* If the temperature is below 20, say that it is "too cold"
* If the temperature is above 27, say that it is "too hot"

3) Create a program that allows the user to input the sides of any triangle, and then return True/False to indicate if the triangle is a Pythagorean Triple or not.

4) Write a program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

5) Write a program to check a triangle is equilateral, isosceles or scalene. An equilateral triangle is a triangle in which all three sides are equal. A scalene triangle is a triangle that has three unequal sides. An isosceles triangle is a triangle with (at least) two equal sides.

6) Write a program to construct the following pattern, using a nested for loop.

```text
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
```

7) The fibonacci sequence is created by summing the two previous numbers together. The first 10 numbers in the sequence are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55. Use a `while()` loop to create a program that will calculate the n-th number of the sequence. For instance, if asked for the 8th number, it should provide the answer of 21.

8) Write a program to check the validity of password input by users. The rules for a valid password are:

* At least 1 letter between [a-z] and 1 letter between [A-Z].
* At least 1 number between [0-9].
* At least 1 character from [$#@].
* Minimum length 6 characters.
* Maximum length 16 characters.

9) Write a program that will allow a user to input his name. The prompt and input data would look something like this: `Please enter your name: Peter Ustinov`. Using a for-loop and the String method, `substring()`, produce a printout of the reversal of the name. For example, the name Peter Ustinov would be: `vonitsu retep`. Ensure that the printout is in all lower-case.

10) If we didn't do it as an example together in class (or you are using my notes online), create a simple number guessing game. The program needs to work as follows:

* The computer picks a random number and stores it as a secret number
* Ask the user to guess the number
* If the guess is higher than the secret number, print the message "too high"
* If the guess is lower than the secret number, print the message "too low"
* If the guess is correct, print the message "you are correct!"
* To use a while loop to keep the game going until the correct guess has been made
* Bonus points: Can you keep count of the number of guesses it takes the player to get it correct?

Note: in Python to generate a random number, you should `import random` at the top of your program, and then use an instruction such as `r = random.randint(0, 100)` to generate a random integer between 0 and 99.

