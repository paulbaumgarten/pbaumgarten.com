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
    a = 2 * PI * radius ** 2
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
    a = 2 * PI * radius ** 2
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
