# Unit 3: Data and logic

## What is data?

Ultimately everything in a computer is reduced to either the presence or absence of an electrical charge. This electrical charge inside transistors is scaled up to form basic circuits that can be used to remember information (ie: act as memory) and perform calculations.

At the heart of it all is the transistor which is a simple electrical switch that can be turned on or off via an electrical signal. A modern Intel CPU has about 1.75 billion transistors in a piece of silicon the size of a fingernail, or 17.185 million transistors per square millimetre. (1)

## The logic gates

We mentioned before that at the most simple level, everything inside a microprocessor is reduced to transistors. But what exactly is a transistor? how does it function? How can such a simple device create the seeming complexity of modern computers?

A transistor is a switch that controls another switch. For a great introduction to how transistors can be combined to create interesting functionality, watch this brief video...

    Relays and Logic Gates - How to Make a Computer: Part I (6:30)
    [https://www.youtube.com/watch?v=fB85NrUBBhQ](https://www.youtube.com/watch?v=fB85NrUBBhQ)

This video introduced you to logic gates. This is the level of complexity from the transistor. We use multiple transistors to build logic gates. Multiple logic gates can then be used in clever patterns to create memory and perform calculations. Once we have the ability to store values in memory, and to be able to perform calculations on those values, we then have the basic building blocks of every computer.

## Truth tables

Produce truth tables for various circuits.

    TODO

---

## Exercise: Creating gates from transistors

We are going to see how logic gates can be physically constructed from simple transitors.

To do this we are going to use a breadboard. It is a simple device that allows us to connect the wires (terminals) of various electronic components together in a simple fashion without having to bother with soldering.

![](img/breadboard.jpg)

The lines marked above show you how the pin holes on the breadboard are interconnected. This means we can put two pins in the same center row and they will become electrically connected.  This allows us to combine components together to make a circuit as the following demonstrates.

<img src="img/breadboard-2.png" width="50%">

Follow the light green shading on the above. That is the path the electricity is travelling.

Before going any further you should build the simple push-button and LED scenario sketched out above to test your understanding of how the breadboard functions.

Once you have completed the LED/button exericse, it is time to attempt to wire up some logic gates.

We will be using NPN transistors for our exercise. The NPN transistor is designed to pass electrons from the emitter to the collector (so conventional current flows from collector to emitter). The emitter "emits" electrons into the base, which controls the number of electrons the emitter emits. ... The transistor is kind of like an electron valve. (https://learn.sparkfun.com/tutorials/transistors/all)

The following shows you how the diagram symbol for an NPN transistor correlates to it's physical appearance. You will need to get the order of the pins correct for your circuit to function.

<img src="img/transistor-NPN-PN2222.png" width="50%">

Finally, the following are the transistor wiring diagrams for four of the core logic gates. Can you tell which one should be which? By the way...

* the zig-zag lines on the diagrams... represent your resistors.
* The "funnel" made out of three lines at the bottom... represents the ground or negative end of the power supply.
* The "A" and "B" points should be coming out from push buttons. The other end of those push buttons should connect to your positive power.
* The "6V" is your positive power (6 volts in this case).
* The "Out" should connect to the positive end of an LED. The other pin of the LED should run into your Ground / Negative. (Note: On the LED one pin is longer than the other. The long one is the positive end.)

Partner up with someone, roll up your sleeves, and figure out the electronics.

![](img/and-gate.gif)

![](img/or-gate.gif)

![](img/nand-gate.gif)

![](img/nor-gate.gif)

---

## Exercise: NandGame

[http://nandgame.com/](http://nandgame.com/)

This website allows you to build a virtual computer beginning from just a NAND gate.

Complete the first 6 levels:

* Invert (not)
* And
* Or
* Xor
* Half Adder
* Full Adder

## Logic circuits

Produce circuit diagrams from equations

    TODO

## Bits and bytes

This presence of absence of electricity needs to be simplified for computer scientists to effectively scale it to the complexity of modern computers. For this reason we think of it as `True` and `False` which is then further simplified into `1` and `0`.

This most simple form of data, that is a `1` or `0` is known as a bit.

Again, dealing with thousands of bits at a time isn't practical, so we scale again. The first level of complexity introduced is to group 8 bits together into a `byte`.

If a bit has two possible values, 0 and 1, and a byte consists of 8 bits, how many possible values does a byte have?

The answer, of course, is 256. But did you get there the easy way or the hard way? How long until you worked out the pattern?

| Number of bits | All possible values | Total possiblities | Also known as |
| -------------- | --------------- | ------------------ | ------------- |
| 1              | 0, 1             | 2                  | 2^1           |
| 2              | 00, 01, 10, 11     | 4                  | 2^2           |
| 3              | 000, 001, 010, 011, 100, 101, 110, 111 | 8  | 2^3           |
| 4  | 0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111 | 16 | 2^4 |


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



## References

1. https://www.quora.com/How-many-transistors-are-in-i3-i5-and-i7-processors
2. https://www.includehelp.com/python/binary-numbers-representation.aspx
3. https://pythonspot.com/binary-numbers-and-logical-operators/

