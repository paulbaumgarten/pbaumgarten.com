# 1.10 - Looping through a list/array

So we have these things called arrays... what if we want to run some code on every item in an array? Would I be asking the question if it couldn't be done?! :-p

In the same way we test to see if a value exists inside a list, we can use the for statement to allow us to run code for each value in that list.  There are two different

```javascript
let starwars = ["Luke", "Han", "Leah", "Obi-wan", "Yoda", "Rey", "Finn"];
for (let person of starwars) {          // person is the elements value
    console.log( "Hello "+person );
}
for (let index in starwars) {           // index is the elements index
    console.log( "Hello person "+index+" is "+starwars[index] );
}
```

Note: There is a subtle difference between the two `for ()` loops shown above. The first uses a keyword of `of` and the second uses the keyword `in`. The two loops print different output. Each one is useful in it's own way, so be aware of the two different types and the different results given. 

We can combine the `for` loops with `if` statements to start making more complex code.  Example:

```javascript
let starwars = ["Luke", "Han", "Leah", "Obi-wan", "Yoda", "Rey", "Finn"];
let skywalkers = ["Luke", "Leah"];
for (let person of starwars) {
    if (skywalkers.indexOf( person ) >= 0) {
        console.log( person+" is a Skywalker");
    } else {
        console.log( person+" is not a Skywalker");
    } 
}
console.log("all done!");
```

Notice the additional levels of indentation each time a new code block is opened.

## Exercise 1

Can you figure out how to do the following?

* Create a list with the names of everyone in your class in a mixed up order.
* Have Javascript automatically alphabetize the list
* Print out the names and say whether or not their name starts with a vowel.

## Exercise 2

Can you figure out how to do the following?

* Create a list with the names of everyone in your class in a mixed up order.
* Print out the names and say whether or not each name is alphabetically higher than the name before.

---