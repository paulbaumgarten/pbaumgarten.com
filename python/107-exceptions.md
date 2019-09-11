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
