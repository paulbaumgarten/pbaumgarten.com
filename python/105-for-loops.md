# For loops

> I've decided that `for loops` need their own dedicated section. This will be developed in the coming days/weeks.

## For item in collection

## For number in range

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

