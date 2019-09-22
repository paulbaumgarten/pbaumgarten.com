# Exceptions

* Suggested video [Exceptions in Python](https://www.youtube.com/watch?v=nlCKrKGHSSk&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=31) by Socratica

Given this code...

```python
# What happens if we input 0?
denominator = int(input("Please enter a number: "))
result = 100 / denominator
print(f"100 divided by {denominator} is {result}")
```

Exceptions is about designing a way to respond to errors, anticipated and unforeseen. There are a few different ways we can respond to this issue.

Firstly, we can have a generic "catch every exception" response with a "try and except" set of blocks.

```python
try:    
    denominator = int(input("Please enter a number: "))
    result = 100 / denominator
    print(f"100 divided by {denominator} is {result}")
except:
    print("I can't do that!")
```

If we know what type of errors to anticpate, we can catch those specifically.  To find the error label to use for the exception statement, you can either run the code in such a way as to generate the error (and thus read it from the error statement), or check the [Python Exceptions documentation](https://docs.python.org/3/library/exceptions.html) for the description of each official exception.

```python
try:
    denominator = int(input("Please enter a number: "))
    result = 100 / denominator
    print(f"100 divided by {denominator} is {result}")
except ValueError:
    print("That wasn't a number")
except ZeroDivisionError:
    print("I can't divide by zero")
except:
    print("Unknown error?!?!?!")
```

# Problem set

1. Create a quadratic formula calculator that uses exceptions to detect if there are 0, 1 or 2 solutions; and then return the correct nnumber of correct solutions. (square root of a negative number exception)
2. Write a simple arithmetic calculator that prompts the user to enter two numbers, A and B. Then print the addition, subtraction, multiplication, division and modulus of A and B. Use exception handling to detect division by zero exception.
3. Add to question 2 exception handling to deal with the user not entering valid numbers for A and B.
4. Make a new copy of Question 5 from the Files problem set, with exception handling in case the file does not exist.
5. Add to question 4, to use exception handling in case the user asks for a line number beyond the limits of the list (ie: if there are only 5 lines and the user askes for line 6).

