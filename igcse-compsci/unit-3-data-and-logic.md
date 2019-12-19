# Unit 3: Data and logic

## What is data?

Ultimately everything in a computer is reduced to either the presence or absence of an electrical charge. This electrical charge inside transistors is scaled up to form basic circuits that can be used to remember information (ie: act as memory) and perform calculations.

At the heart of it all is the transistor which is a simple electrical switch that can be turned on or off via an electrical signal. A modern Intel CPU has about 1.75 billion transistors in a piece of silicon the size of a fingernail, or 17.185 million transistors per square millimetre. (1)

## The logic gates

We mentioned before that at the most simple level, everything inside a microprocessor is reduced to transistors. But what exactly is a transistor? how does it function? how can such a simple device create the seeming complexity of modern computers?

In it's most simple form, a transistor is a switch that controls another switch. For a great introduction to how transistors can be combined to create interesting functionality, watch this brief video...

    Relays and Logic Gates - How to Make a Computer: Part I (6:30)
    [https://www.youtube.com/watch?v=fB85NrUBBhQ](https://www.youtube.com/watch?v=fB85NrUBBhQ)

This video introduced you to logic gates. This is the level of complexity from the transistor. We use multiple transistors to build logic gates. Multiple logic gates can then be used in clever patterns to create memory and perform calculations. Once we have the ability to store values in memory, and to be able to perform calculations on those values, we then have the basic building blocks of every computer.

## Truth tables

Produce truth tables for various circuits

## Logic circuits

Produce circuit diagrams from equation

## Bits and bytes

This presence of absence of electricity needs to be simplified for computer scientists to effectively scale it to the complexity of modern computers. For this reason we think of it as `True` and `False` which is then further simplified into `1` and `0`.

This most simple form of data, that is a `1` or `0` is known as a bit.

Again, dealing with thousands of bits at a time isn't practical, so we scale again. The first level of complexity introduced is to group 8 bits together into a `byte`.

If a bit has two possible values, 0 and 1, and a byte consists of 8 bits, how many possible values does a byte have?

The answer, of course, is 256. But did you get there the easy way or the hard way? How long until you worked out the pattern?

| Number of bits | Possible values | Total possiblities | Also known as |
| -------------- | --------------- | ------------------ | ------------- |
| 1              | 0 1             | 2                  | 2^1           |
| 2              | 00 01 10 11     | 4                  | 2^2           |
| 3              | 000 001 010 011 100 101 110 111 | 8  | 2^3           |
| 4  | 0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111 | 16 | 2^4 |


## Converting between denary and binary

    Binary - How to Make a Computer: Part II (7:15)
    https://www.youtube.com/watch?v=NRKORzi5tnM

## Binary use in registers

16, 32, 64 bit computing

## Hexadecimal numbers

Reasoning for hex notation

## Convert hex and denary

## Convert hex and binary

## Common uses of hex in computing

### HTML colours

### MAC addresses

### Assembly languages

### Debugging

# Logic circuits



## References

1. https://www.quora.com/How-many-transistors-are-in-i3-i5-and-i7-processors
