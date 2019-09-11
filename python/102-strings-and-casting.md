# Strings & casting

* If you haven't already watched this video, I suggest you do so now. [Learning Python (2018 edition) 01: Your first programs](https://www.youtube.com/watch?v=dOCTDDxtv7s) (Variables, numbers, strings & casting)

## String variables

A text variable is known as a "string" (a string of characters).

* The starting and end point of the text is denoted by a set of quotes or double quotes.

```python
a = "This is a string"
b = 'This is a string'
c = "This is not a string'
```

## Concatenating strings & f-strings

> f-Strings require a minimum of Python version 3.6

Strings can be concatenated together with the `+` operator.

```python
a = "Hello"
b = "world!"
c = a + " " + b
print(c)
```

A convenient way of inserting the content of other variables is an f-string.

* Preceed the opening quotes with the `f` character
* Wrap variable names with `{}` characters

```python
a = 10
print(f"The value of a is {a}")
```

F-Strings have a variety of methods for formatting the value being inserted into a string.

* Decimal places

```python
val = 12.3
print(f'{val:.2f}')     # 2 decimal places, eg 12.30
print(f'{val:.5f}')     # 5 decimal places, 12.30000
```

* Width

```python
val = 12.3
print(f'{val:10}')      # 10 characters wide, eg "      12.3"
print(f'{val:10.5f}')   # 10 characters wide, 5 decimal places, eg "  12.30000"
```

* Left and right justify (strings default to left justify, numbers default to right justify)

```python
val = 12.3
txt = "Hello"
print(f'{val:<10}')      # 10 characters wide left justify, eg "12.3      "
print(f'{txt:>10}')      # 10 characters wide right justify, eg "     Hello"
```

* Hexadeciaml notation

```python
num = 255
print(f"{num:x}")       # Hexademcimal value, eg "ff"
```

*Credit: http://zetcode.com/python/fstring/*

## Inputting strings

We can prompt the user to input data and store it into a string using the `input()` command.

```python
person_name = input("What is your name?")
print(f"Hello {person_name}")
```

## Sub strings

To extract parts of a string we use a set of square brackets after our variable name. 

```python
name = "Luke Skywalker"
print( name[5:] )
print( name[5:8] )
print( name[:4] )
print( name[-9:] )
```

* String positions start from zero
* The bracket notation works as `[ after_this_position : up_to_this_position ]`
* If you omit the first value, the beginning of the string is used
* If you omit the second value, the end of the string is used

## String functions

String functionality

```python
name        = "Luke Skywalker"
length      = len(name)
space_at    = name.index(" ")
father      = name.replace("Luke", "Anakin")
occurances  = name.count("a")
tmp         = name.lower()
tmp         = name.upper()
tmp         = name.title()
tmp         = name.swapcase()
tmp         = name.ljust(30)    # Left justify with spaces to length 30
tmp         = name.rjust(30)    # Right justify with spaces to length 30
```

Example usage:

```python
name = "Luke Skywalker"
space = name.index(" ")
given_name = name[:space]
family_name = name[space+1:]
```

## Casting

Converting between datatypes is known as casting. 

```python
f = float( 100 )
i = int( 13.7 )
i = int( "13" )
f = float( "13.7" )
s = str( 13.7 )
```

Initially you will find it most useful to convert the String from `input()` into number types.

```python
n = float(input("Please enter a number"))
result = n * 2
print(f"Double your number is: {result}")
```

## Problem set

1. For any string that consists of exactly two words with one space separating them, swap the two words around. For example: Given the string `Hello world!`, have the program print `world! Hello`.
2. Given a sentence input, return how many words are in the sentence. For example, `The quick brown fox jumps over the lazy dog.` is `9` words.
3. Given a string input of a date in format, `dd/mm/yyyy`, print an output advising the current day, month and year number.
4. Given a string, return a new string made of 3 copies of the last 2 chars of the original string. Assume the input string length will be at least 2 characters. For example, the string "Hello" should be result in "lololo".
5. Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
6. Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
7. Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1. For example, strings "Hello" and "There" should result in "ellohere".
8. How would you print the following? `All "good" men should come to the aid of their country.` (ie: how to print the double quote character)
9. Write code that will produce the following printout using only a single print() function call. 

```txt
Hello
Hello again
```
