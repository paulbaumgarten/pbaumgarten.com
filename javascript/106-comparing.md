# 1.6 - Comparing values

The power of programming comes from letting the computer do work for us. To do that it needs to make decisions. Javascript can make decisions on the basis of comparing one value to another.

For instance, check to see what Javascript will print for the following statements:

```javascript
console.log( 1 === 1 );
console.log( 1 === 0 );
console.log( "a" === "a" );
console.log( "a" === "A" );
console.log( "a" !== "z" );
console.log( 1 > 0 );
console.log( -1 > 0 );
console.log( 2 >= 3 );
console.log( -3 < -1 );
console.log( 3 < 1 );
console.log( 2 <= 3 );
console.log( 2 === 2 && 3 === 3 );
console.log( 4 === "4" );   // What's the difference with the triple and double equality sign?
console.log( 4 == "4" );
```

As a summary of the different symbols and what they mean:

* `a === b` ... is equal to
* `a !== b` ... is not equal to
* `a > b` ... greater than
* `a >= b` ... greater than or equal to
* `a < b` ... less than
* `a <= b` ... less than or equal to
* `a === 0 && b === 0` ... both are true
* `a === 0 || b === 0` ... either are true

## Common mistake: Assignment or comparison?

Take careful note of the difference in punctuation between setting a value to a variable, and comparing two values! Setting a variable to a given value uses the single equal sign `=` whereas comparing two values or variables uses the triple equal sign `===`. (You may see some Javascript documents suggest using the double equal sign for comparison purposes, until you've been programming long enough to understand the technical risk involved, stick with the triple, it's "safer").

## Exercises

What would this do?

```javascript
let response = prompt("Type a number: ");
let n = Number(response);
console.log( "Is your number bigger than 10?" );
let result = n > 10;
console.log( result );
```

How is this one different?

```javascript
let response = prompt("Type a number: ");
let n = Number(response);
let result = n > 10 && n < 100;
console.log( result );
```

Here is an example checking to see if one string appears inside another:

```javascript
let secret = "abracadabra";
let letter = prompt("Guess a letter: ");
console.log( "Is your letter inside the secret word? " );
let answer = secret.indexOf(letter) >= 0;
console.log( answer );
```

---