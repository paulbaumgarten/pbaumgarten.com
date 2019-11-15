# Lists

* Video: [Learning Python (2018 edition) 03: Lists and loops](https://www.youtube.com/watch?v=s3v0GtnyeWM) (lists, for loops)

## Why use lists?

A list (known as an array in most other languages) allows us to store a list/set/collection of values all assigned to one variable identifier. They are very useful when we have a collection of values that are similar in nature and that will be processsed in the same manner.

For example, supposed we are keeping record of test scores obtained by a group of students. Without a list we could use something like the following:

```python
score1 = 59
score2 = 92
score3 = 85
score4 = 61
score5 = 78
```

Supposed we want to calculate the highesst, lowest and average score? That would look like...

```python
highest = score1        # Initially set highest to the first value
if score2 > highest:
    highest = score2
if score3 > highest:
    highest = score3
if score4 > highest:
    highest = score4
if score5 > highest:
    highest = score5
lowest = score1         # Initially set lowest to the first value
if score2 < lowest:
    lowest = score2
if score3 < lowest:
    lowest = score3
if score4 < lowest:
    lowest = score4
if score5 < lowest:
    lowest = score5
average = (score1 + score2 + score3 + score4 + score5) / 5
print(f"The highest score was {highest}, the lowest was {lowest} and the average was {average}")
```

You can see that the whole process will quickly get very tedious. There will be a lot of copy-and-pasting-and-renaming of code going on. Imagine if we needed to scale this up to 100 students for an entire year group? Unmanagable and error prone!

Enter the list!

The equivilant task using lists might look like

```python
scores = [59, 92, 85, 61, 78]
highest = scores[0]     # Initially set highest to the first value
lowest = scores[0]      # Initially set lowest to the first value
total = 0               # Running total for calculating the average later
for value in scores:    # Iterate through each `value` within `scores`
    if value > highest:
        highest = value
    if value < lowest:
        lowest = value
    total = total + value
average = total / len(scores)
print(f"The highest score was {highest}, the lowest was {lowest} and the average was {average}")
```

Our scores array can easily contain 1000s of records and we would not have to change a single line of the calculations code! Arrays can be extremely useful!

## Creating a lists (or array)

As already said: A list (known as an array in most other languages) allows us to store a list/set/collection of values all assigned to one variable identifier.

Examples

```python
primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
vowels = ["A", "E", "I", "O", "U"]
starwars = ["Luke", "Han", "Leah", "Obi-wan", "Yoda", "Rey", "Finn"]
empty_list = []
```

Syntax notes:

* The square brackets denotes the beginning and end of the list collection
* Items in a list are separated by commas

## Manipulating a list

Adding items

```python
starwars = ["Luke", "Han", "Leah", "Obi-wan", "Yoda", "Rey", "Finn"]
starwars.append("BB-8")     # Append to end of the list
starwars.insert(0, "R2-D2") # Insert to position 0
```

Combining lists

```python
starwars = ["Luke", "Han", "Leah", "Obi-wan", "Yoda", "Rey", "Finn"]
darkside = ['Vader', 'Palpatine']
characters = starwars + darkside
```

Removing items

```python
starwars.remove("Han")      # Remove by item value
starwars.pop(0)             # Remove by item position
```

Overwriting an item

```python
conflicted = ['Anakin', 'Kylo']
conflicted[0] = "Darth Vader"   # He turned!
```

## Sublists

Given a string is conceptually just a list of characters, it should be no surprise the same setset functionality of strings works for lists.

What is the value of partial after each line?

```python
starwars = ["Luke", "Han", "Leah", "Obi-wan", "Yoda", "Rey", "Finn"]
partial = starwars[3:]
partial = starwars[:3]
partial = starwars[-1:]
```

## Other list functions

```python
numbers = [36, 9, 13, 71, 58, 95, 22]
result = min(numbers)
result = max(numbers)
result = len(numbers)
result = sum(numbers)
numbers.sort()                  # Sorts the current list
numbers.reverse()               # Reverses the currnent list
position = numbers.index(13)    # What position location is 13 at?
occurances = numbers.count(9)   # How many occurances of 9 appear?
is_inside = 13 in numbers       # Does the item 13 appear in list numbers?
```

## Splitting and joining lists

Splitting string into a list

```python
saying = "May the force be with you"
words = saying.split(" ")
print(words)
```

A more useful example

```python
birthdate = input("Your date of birth as dd/mm/yyyy:")
parts = birthdate.split("/")
day = int( parts[0] )
month = int( parts[1] )
year = int( parts[2] )
```

Joining a list into one string

```python
delimiter = " "
parts = ["I", "am", "Groot"]
groot = delimiter.join(parts)
print(groot)
```

## Traversing a list

We can traverse over a list using a 'for-loop'. This is a loop that increments over a series of values, running the intended code with a different value each time.

There are two methods of writing for-loops. 

### Method 1: For item in collection

The **item in collection** method will, when provided a list of values, the for-loop will iterate through each value. In the following example, the variable `character` shall have the value `Luke` the first time the loop is executed, `Han` the second time, `Leah` the third time and so on until the list is complete.

```python
starwars = ["Luke", "Han", "Leah", "Obi-wan", "Yoda", "Rey", "Finn"]
for character in starwars:
    print(f"Vote for {character} as your favourite starwars character")
```

### Method 2: For value in range

The **value in range** method will increment of a series of numbers. In the example below, the `range(10)` function generates a sequence of values from `0` up to but not including `10`. So, the print will generate the output of `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`.

```python
for i in range(10):
    print(i)
```

You can still use this method to work in combination with lists, by using the `len()` function to determine the length of a given list, and then use the square bracket notation to access individual list elements, as the following example illustrates.

```python
starwars = ["Luke", "Han", "Leah", "Obi-wan", "Yoda", "Rey", "Finn"]
for i in range( len( starwars ) ):
    print(f"Character #{ i } is { starwars[i] }")
```

## For-loops for non-list purposes

You can also use a for-loop for any iteration when you know the number of iterations you wish to loop in advance.

For instance, to increment from 10 to 19 would look like:

```python
for i in range(10, 20):
    print(i)
```

The following example shows how you can change the amount you increment each time. This will print `0`, `5`, `10`, `15`, `20`, and stop after printing `95`.

```python
for i in range(0, 100, 5):
    print(i)
```


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

## Tips and tricks

```python
# Python's list comprehension is a great little short cut...
vals = [expression for value in collection if condition]

# The long form equivilant is...
vals = []
for value in collection:
    if condition:
        vals.append(expression)
```

For example:

```python
nums = [ x*x for x in range(10) if not x % 2 == 0 ]
print(nums)   # [0, 4, 16, 36, 64]
```

## Problem set

For some introductory level questions, I recommend solving the problem sets on coding bat:

* [List-1 coding.bat problems (no loops)](https://codingbat.com/python/List-2)
* [List-2 coding.bat problems (require 1 loop)](https://codingbat.com/python/List-2)

Be warned, a number of the questions in the main problem set are quite challenging for new programmers. Do not worry if you feel some of them are beyond you if you are at the beginning stags of learning to program. Revisit the questions you can't do after you have been programming consistently for about 12 months.

1. Write a program to sum all the items in a list.
2. Write a program to get the largest number from a list.
3. Write a program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
4. Write a program to remove duplicates from a list.
5. Write a function that takes two lists and returns True if they have at least one common member.
6. Write a program to print a specified list after removing the 0th, 4th and 5th elements. Sample List : `['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']` Expected Output : `['Green', 'White', 'Black']`
7. Write a program to print the numbers of a specified list after removing even numbers from it.
8. Write a program to select an item randomly from a list, which is then removed from the original list so it can’t be re-drawn (just like a deck of cards scenario)
9. Write a program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
10. Given two lists, write a program to print the items that are not in both lists.
11. Write a program to append the items from one list to a second list.
12. Write a program for computing primes upto 1000. Hint: Google for the Sieve of Eratosthenes

For question 8, you may like to copy and paste the following as a list to use:

```python
deck = [
    "A♥️", "2♥️", "3♥️", "4♥️", "5♥️", "6♥️", "7♥️", "8♥️", "9♥️", "10♥️", "J♥️", "Q♥️", "K♥️",
    "A♥️", "2♠️️", "3♠️", "4♠️", "5♠️", "6♠️", "7♠️", "8♠️", "9♠️", "10♠️", "J♠️", "Q♠️", "K♠️",
    "A♦️", "2♦️", "3♦️", "4♦️", "5♦️", "6♦️", "7♦️", "8♦️", "9♦️", "10♦️", "J♦️", "Q♦️", "K♦️",
    "A♣️", "2♣️", "3♣️", "4♣️", "5♣️", "6♣️", "7♣️", "8♣️", "9♣️", "10♣️", "J♣️", "Q♣️", "K♣️",
]
```
