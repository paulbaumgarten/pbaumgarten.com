# 1.5 - Converting between numbers and strings

Converting between strings and numbers is particularly useful if we want to use `prompt()` to get a number from the user. Without this step `prompt()` genreally assumes what it receives is text rather than a number, and just because we ask the user to type a number doesn't mean they will, so it always pays to double check the content of a variable we have reeived from a user rather than just assuming it to be valid.

We can convert from text strings to numbers, and then back again for printing purposes.

Converting a string to a number

```javascript
let s = prompt("Type an integer:");
let n = Number(s);             // n is a number you can perform calculations on
console.log( 2 * n );
```

Converting a number to a string

```javascript
let a = 4;
let s = a.toString();
console.log("Your number is " + s);
console.log( a + a );
console.log( s + s );     // Notice the differnece in output these two sets of additions give
```

Example:

```javascript
let number_text = prompt("Type an integer:");
let n = Number( number_text );
let answer = n * 2;
console.log("Double your number is: "+answer);
```

## Exercise

Create a program that asks for two numbers, and then prints out:

* The addition of those two numbers
* The subtraction of the first number minus the second
* The multiplication of the two numbers
* The division of the first number divided by the second. Example screen of the expected result:

---