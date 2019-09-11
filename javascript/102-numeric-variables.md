# 1.2 -  Numeric variables

What is a variable? A variable is just a name we assign to a piece of memory on the computer. The is similar to the memory button you are used to on the calculator, except we can have as many variables (memory locations) as we want, and we can give them names.

In a new file (perhaps named `numbers-2.html`, we are going to create a variable called "x" and give it a value of 5:

```javascript
let n = 4;
```

The keyword `let` tells Javascript you are about to create a variable. You can read that line of code as "let the variable n be assigned to the value of 4".

Ok, one last time because I"m so good to you, I'll give you the full HTML just to make sure you get the idea:

```html
<html>
    <body>
    </body>
    <script type="application/javascript">
    "use strict";

let n = 4;

    </script>
</html>
```

## A common mistake: Case sensitivity

Javascript is case-sensitive when it comes to variable names. Upper case `N` is treated as a different name to lower case `n`. This is important to remember as one of the most common mistakes students make is changing the spelling of their variable names and wondering why it doesn't work.

It's easy enough to demonstrate this through the following code:

```javascript
let n = 4;
let N = 15;
console.log( n );
console.log( N );
```

You'll notice one has not affected the other, they are treated as two seperate distinct memory locations. Please don't get your variable names mixed up!

## Using variable names in my calculations

The same way we did math before by typing in the actual numbers, we can do the same thing by substituting a number with a variable name. Javascript will automatically look up the variable's value and use it in the calculation.

```javascript
let x = 4;
console.log( 2 * x );
console.log( x - 5 );
```

What names can we use for variables?

* Anything alpha-numeric – which is to say any combination of letters and numbers.
* The only punctuation allowed is the underscore _
* The name must start with a letter or an underscore _ (not a number)
* Spaces and other symbols are not allowed

What will Javascript print in the last line of this example?

```javascript
let eggs_per_cake = 3;
let number_of_cakes = 10;
let total_eggs = eggs_per_cake * number_of_cakes;
console.log( total_eggs );
```

---

## A common mistake: Incorrectly writing calculations

When doing a calculation to save the result in a variable the rule is that the value or calculation goes on the right of the assignment sign (what you think of as the "equal sign"), the name of the variable we want to save the answer to goes on the left of the assignment sign. ie:

```javascript
let save_to_me = use_my_value + some_other_value;
```

## Exercises

Some practice exercise with doing simple calculations and variables:

1. Write a program that for any set number, will print out what the number before it was and the number after it. For example, if given the number 179, the output would be: `180` and `178`.

2. Write a program that for any number of seconds, will let you know how many hours, minutes and seconds this converts to. For example `4030` would output `1` for hours, `7` for minutes and `10` for seconds.

3. Write a program that will extract the 10s digit from a number. For example, the tens digit in 1234 is `3`.

---