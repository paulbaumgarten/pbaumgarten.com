# Functions

* Suggested video [Python Functions](https://www.youtube.com/watch?v=NE97ylAnrz4&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=12)  by Socratica

## Introducing functions

Functions are blocks of code that you assign a name to. You can use that name to easily run that code again whenever you need.

Functions are very useful for separating common tasks out from your main code. It allows you to avoid repeating yourself all the time which makes your code easier to maintain. Tasks like reading from a file, saving to a file, etc are all ideally suited to being chopped off into a separate function. 

> Think of an Icecreamary
> 
> Lots of different possible flavours, toppings, numbers of scoops, choice of waffle or regular cone, etc.
>
> One person could order a double scoop of chocolate fudge and vanilla on a waffle cone, where as the next customer might ask for a cup of raspberry sorbet with nut sprinkles. The salesperson calculates the cost for each and advises each custoemr on the price. In order to calculate that cost there are a number of inputs (number of scoops, type of cone, etc) and an output (price). How it is actually calculated is not important, provided it is trustworthy and works reliably. 
>
> In this way a function can provide a "black box" model through which we can create an abstraction to represent our problem. 
>
> Programmers need to know how to (a) use other peoples abstractions and (b) be able to create their own. For now, the abstraction we are concerned with is creating a function.

A couple of examples:

```python
def area(radius):
    PI = 3.1415
    a = PI * radius ** 2
    return a

def circumference(radius):
    PI = 3.1415
    circ = 2 * PI * radius
    return circ

# Prompt the user for a radius
r = int(input("What is the radius of your circle?"))

# Execute our custom functions
answer1 = area(r)                
answer2 = circumference(r)       

# Print our results
print(f"The area of your circle is: {answer1}")
print(f"The circumference of your circle is: {answer2}")
```

## Syntax explainer

Functions:

* The `def` keyword denotes you are defining a function.
* You must have the parenthesis after the function name. If no parameters are required, just them empty.
* Like previous uses, indentation is used to indicate which code belongs to the function. Return to the previous level of indentation when the function is complete.
* The return at the end of the function is optional. If there is no result to pass back to the code that called it, you can skip it.

## Functions in seperate files

Putting functions you will frequently reuse in different files makes it easy to import them into other projects later.

**File: circles.py**

```python
def area(radius):
    PI = 3.1415
    a = PI * radius ** 2
    return a

def circumference(radius):
    PI = 3.1415
    circ = 2 * PI * radius
    return circ
```

**File: main.py**

```python
# Import the circles file
import circles              

# Prompt the user
r = int(input("What is the radius of your circle?"))

# Execute our functions
answer1 = circles.area(r)
answer2 = circles.circumference(r)

# Output the results
print(f"The area of your circle is: {answer1}")
print(f"The circumference of your circle is: {answer2}")
```

## Default and optional parameter values

```python
def greetings( given_name, family_name=None ):
    # Providing a family_name is optional in this example
    if family_name:
        print(f"Hello {given_name} {family_name}")
    else:
        print(f"Hello {given_name} Doe")

greetings("Jane", "Smith")
greetings("John")
```

## Functions for user input validation

Functions can be a handy way to require the user to comply with our wishes to enter information in a particular manner. By the time we write the checking/validation code and the loop, user input checks can run to several lines, and it would be quite common within a simple program to want to validate the same style of input several times. Functions make a handy way to reuse code for this purpose.

```python
def confirm( prompt ):
    loop = True
    response = ""
    while loop:
        response = input( prompt )
        if response == "y" or response == "n":
            loop = False
        else:
            print("Only a 'y' or 'n' character are accepted, please try again.")
    return response
```

# Problem set

1. Create a function `area_right_angled_triangle(base, height)` that returns the calculated area.

2. Create a function `area_non_right_angled_triangle(base, height, angle)` that returns the calculated area (remember you will need to convert the angle to radios before using it with the sine function).

3. Create a user input validation function that requires the input of a number.

4. Create a user input validation function that requires the input of a phone number (so `+`, spaces and `-` characters are permitted).

5. Create a user input validation function that requires the input of a date in the `dd/mm/yyyy` format. Bonus points if you ensure that the `dd`, `mm` and `yyyy` values make sense (ie: day should be between 1 and 31).

6. Create a user input validation function that accepts a list of strings as the parameter and presents them to the user as a list of menu choices, requiring the user to enter a number corresponding to a valid choice before proceeding. For example if the code to run the funciton was....

```python
menu = ["Open file", "Save file", "Quit program"]
choice = menu_picker( menu )
print( f"You choose option {choice}" )
```

The output could look like...

```text
Your choices are:
1. Open file
2. Save file
3. Quit program
Please enter a number from 1 to 3:
```





