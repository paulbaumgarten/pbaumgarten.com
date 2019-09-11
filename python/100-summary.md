# Python summary for beginners

This summary is not intended as a teaching guide but a reminder prompt on how to use some the key parts of Python. Use this **after** doing the relevant lessons.

Updated: February 2019 by P.Baumgarten

## Print and input

To print text to screen:

```python
print("hello")
```

To print a variable to screen:

```python
name = "Han Solo"
record = 12
print(f"{name} completed the Kessel run in {record} parsecs")
# notice the 'f' in front of the first set of quotes
```

To ask the user to type input

```python
name = input("What is your name? ")                         ## Input saved as text
num = int(input("Type an integer between 1 and 100: "))     ## Input saved as an integer
double = num * 2
print(f"Hello {name}, double your number is {double}")
```

## Numbers

Python has two types of numbers, integers and floats. Integers are "whole numbers" without decimals, floats are th name given to numbers that contain decimals.

To get the result of a mathematical calculation, put the equation on the right of an equal sign, and the variable you wish the answer saved in on the left of the equal sign.

Arithmetic

```python
a = 100
b = 6
c = a + b           # addition          ... c == 106
c = a - b           # subtraction       ... c == 94
c = a * b           # multiplication    ... c == 400
c = a / b           # division          ... c == 16.66667
c = a // b          # integer division  ... c == 16
c = a % b           # modulus remainder ... c == 4 (ie: remainder of 100 divided by 6)
c = a ** b          # exponent          ... c == 1000000000000 (ie: 10^6)
```

Geometry and trigonometry

```python
import math         # add this line to the top of your program for the math functions to work
```

* `math.pi` - returns value of pi with as much precision as available to your computer
* `math.hypot( a, b )` - returns the hypotenuse for a right angled triangle with side lengths a and b 
* `math.sin( radians )` - returns the sin() for an angle provided in radians
* `math.cos( radians )` - returns the cos() for an angle provided in radians
* `math.tan( radians )` - returns the tan() for an angle provided in radians
* `math.asin( ratio )` - returns the inverse sin() for a ratio. answer provided in radians
* `math.acos( ratio )` - returns the inverse cos() for a ratio. answer provided in radians
* `math.atan( ratio )` - returns the inverse tan() for a ratio. answer provided in radians
* `math.degrees( radians )` - convert angle from radians to degrees
* `math.radians( degrees )` - convert angle from degrees to radians

---

## Strings

Assign a text string a value

```python
s = "Hello"
```

Searching strings

```python
s = "To infinity and beyond!"
if "infinity" in s:
   print("Yes, the word infinity is in the string")
else:
   print("No, the word infinity is not in the string")
```

Get substrings

* String positions start from 0. That is, the first letter is position 0, the second letter is position 1 and so forth.
* When asking for a range of characters, Python will give you a substring that includes the starting position number, but not including the end position number.

```python
s = "To infinity and beyond!"
s2 = s[:2]                  ## Get from start until position 2. s2 == "To"
s2 = s[16:]                 ## Get from position 16 to end. s2 == "beyond!"
s2 = s[3:11]                ## Get from position 3 up to not including position 11. s2 == "infinity"
```

Changing strings

```python
s = "To infinity and beyond!"
s2 = s.lower()              ## s2 == "to infinity and beyond!"
s2 = s.upper()              ## s2 == "TO INFINITY AND BEYOND!"
s2 = s.title()              ## s2 == "To Infinity And Beyond!"
s2 = s.swapcase()           ## s2 == "tO INFINITY AND BEYOND!"
s2 = s.ljust(30)            ## s2 == "To infinity and beyond!       "
s2 = s.rjust(30)            ## s2 == "       To infinity and beyond!"
s2 = s.replace(" ", "--")   ## s2 == "To--infinity--and--beyond!"
```

Query content of string

```python
s = "To infinity and beyond!"
n = len(s)                  ## get length of string ... n == 23
n = s.count(" ")            ## count spaces in string ... n == 3
n = s.index("o")            ## position of first 'o' in the string ... n == 1
n = s.rindex("o")           ## position of last 'o' in the string ... n == 19
result = s.isnumeric()      ## does it contain only numbers?
result = s.isalpha()        ## does it contain only letters?
result = s.islower()        ## is it all lowercase?
result = s.isupper()        ## is it all uppercase?
result = s.istitle()        ## is it all title case?
result = s.isspace()        ## is it all spaces?
```

---

## If

To execute an "if" statement consists of two parts: Firstly the question you wish to ask, then the code you want to run if the answer to that question is True.

To ask a question, we generally ask Python to compare two or more values to see if they obey a rule.

Examples of number comparisions we can ask include:

```python
print( 1 == 1 )             ## Is 1 equal to 1              ... True
print( 1 == 0 )             ## Is 1 equal to 0              ... False
print( "a" == "a" )         ## Is "a" equal to "a"          ... True
print( "a" == "A" )         ## Is "a" equal to "A"          ... False
print( "a" != "z" )         ## Is "a" not equal to "z"      ... True
print( 1 > 0 )              ## Is 1 greater than 0          ... True
print( -1 > 0 )             ## Is -1 greater than 0         ... False
print( 2 >= 3 )             ## Is 2 greater or equal to 3   ... False
print( -3 < -1 )            ## Is -3 less than -1           ... True
print( 3 < 1 )              ## Is 3 less than 1             ... False
print( 2 <= 3 )             ## Is 2 less or equal to 3      ... True
```

**Important note:** When asking comparisions, we use a double equal sign! A single equal says we want to **set** the value not ask if they are a match.

We can also query string content such as:

```python
s = "May the force be with you!"
print(s == "Join the dark side")        ## False... they are not the same
print("the" in s)                       ## True... "the" appears in the content of 's'
```

We can also join multiple queries together such as

```python
a = int(input("Enter a number: "))
print( a > 0 and a < 10 )       ## Is number 'a' greater than 0 and less than 10?
print( a < 0 or a > 10 )        ## Is number 'a' less than 0, or is it greater than 10?
```

Once we have our query figured out, we can construct our "if" statement.

```python
a = int(input("Enter a number: "))
if (a > 10):
    print("a is bigger than 10")
elif (a > 0):
    print("a is bigger than 0 but not bigger than 10")
elif (a == 0):
    print("a is zero")
else:
    print("a is less than 0")
```

Note, the "if" statement will keep asking questions of the various 'elif' until it finds one that is True. After one item is True, it will skip the rest of the options available and jump to the next thing after the "if" statement is all finished.

---

## While loops

The "while loop" works very similar to the if statement. The difference being that so long as something is True, it will keep running the same indented section of code. An example:

```python
up_to = int(input("Enter a number for me to count up to: "))
num = 1
while num <= up_to:
   print( num )
   num = num + 1
print("The end!")
```

## For loops

You can also use a for-loop when you know the number of iterations you wish to loop in advance.

```python
limit = int(input("Enter a number for me to count up to: "))
for i in range(limit):   # will loop from 0 to up_to-1
   print( i+1 )
print("The end!")
```

You can also specify a starting number other than zero. For instance

```python
for i in range(50, 100):   # will loop from 50 to 99
   print( i )
print("The end!")
```

You can even specify that it counts downwards, or using an interval different to one by specifying a third parameter to the `range()` function.

```python
for i in range(100, 0, -1):   # will loop from 100 to 1
   print( i )
print("The end!")
```

## Lists and for-loops

A list is a means of storing multiple values to one variable name. Other programming languages call these 'arrays'.

Example lists:

```python
primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
vowels = ["A", "E", "I", "O", "U"]
starwars = ["Luke", "Han", "Leah", "Obi-wan", "Yoda", "Rey", "Finn"]
```

Lists have many of the same features of strings (which is really just a list of characters) to query them and get sub-parts from.

```python
size = len( starwars )              ## How many items in the starwars list
first = starwars[0]                 ## Get the first item in the starwars list
second = starwars[1]                ## Get the second item in the starwars list
last = starwars[-1]                 ## Get the last item in the starwars list
starwars.append("Darth Vadar")      ## Add an item to the starwars list
"Luke" in starwars                  ## Is "Luke" in the starwars list?
starwars.sort()                     ## Sort the list into alphabetical or numerical order
smallest = min(primes)              ## Get the smallest value from the list
largest = max(primes)               ## Get the largest value from the list
```

We can also use a `for` loop to process every item in a list

```python
starwars = ["Luke", "Han", "Leah", "Obi-wan", "Yoda", "Rey", "Finn"]
for character in starwars:
    print(f"{character} is a person in Starwars")
```
