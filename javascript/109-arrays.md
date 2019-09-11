# 1.9 - Making a list/array

So far we've talked about numbers, strings and booleans where each variable just stores one thing at a time. What happens if we want to manage a shopping list, or a list of students in my class... and I want to be able to manage that entire list of things together? Javascript allows us to create lists, which in programmer-speak are called arrays.

Here are three arrays:

```javascript
let primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23];
let vowels = ["A", "E", "I", "O", "U"];
let starwars = ["Luke", "Han", "Leah", "Obi-wan", "Yoda", "Rey", "Finn"];
```

The two key tips to making an array:
* Javascript knows it is a list because of the square brackets!
* Items in a list are separated by commas!

See if you can intuitively work out how the following various commands behave, and then code them up to check.

```javascript
let starwars = ["Luke", "Han", "Leah", "Obi-wan", "Yoda", "Rey", "Finn"];
console.log( starwars.length );
console.log( starwars[0] );
console.log( starwars[1] );
console.log( starwars[2] );
console.log( starwars[-1] );
console.log( starwars );
```

After doing the above, can you guess what this will do?

```javascript
let starwars = ["Luke", "Han", "Leah", "Obi-wan", "Yoda", "Rey", "Finn"];
starwars.push("Darth Vader")
console.log( starwars.length );
console.log( starwars[ starwars.length - 1 ] );
console.log( starwars );
```

We can also use the `indexOf()` comparison test we used for strings with arrays.

```javascript
console.log( starwars.indexOf("r2d2") );
console.log( starwars.indexOf("Leah") );
```

Just like strings, we also have a `.slice()` function available for arrays.

What would these do?

```javascript
console.log( starwars.slice(0,2) );
console.log( starwars.slice(1,3) );
console.log( starwars.slice(0,3) );
console.log( starwars.slice(3) );
```

How will this behave?

```javascript
starwars.sort();
console.log( starwars );
```

---