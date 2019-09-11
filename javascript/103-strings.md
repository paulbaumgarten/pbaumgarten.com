# 1.3 - String variables (text)

Suppose we want to print some kind of text message to the user? We can print text very easily, just start and end the text with a set of quotations. You already saw this in our very first program:

(oh, time for a new file. Call this `strings-1.html` or similar)

```javascript
console.log( "Hello world");
```

Just as we can use variables to store numbers, we can also use them to store text. We enclose the contents of our text in a set of double quotes " as shown:

```javascript
let name = "Mr Baumgarten";
console.log( name );
```

Also just as we can add numbers together, we can "add" these text variables together too! Obviously there is no calculation involved, instead what happens is it joins the two bits of text together.

```javascript
let person = "Mr Baumgarten";
let message = "Hello ";          // Notice: the space at the end before the closing quote.
console.log( message + person );
```

If we change the value of the text variables, Javascript will reflect the change next time you perform the calculation.

```javascript
let person = "Mr Baumgarten";
let message = "Hello ";
console.log( message + person );
person = "Luke Skywalker";        // Notice: why no "let" ???
console.log( message + person );
```

We only use `let` when we are telling Javascript that we are creating a **new** variable. When we just want to modify an existing one, we don't use `let`. If we had included the `let` keyword, we would have received an error in the console like the one below, advising us we are trying to create a new variable with a name that has already been used.

![Screenshoot](img/js-let-error.png)

Variables that contain a bit of text for their value are known in the programming world as **strings**.

## Getting the length of a string

It can be handy to get the length of a string. Javascript gives us a very useful tool for this called `.length`. The `.length` property will give us a number indicating how many characters are in our text string.

```javascript
let person = "Mr Baumgarten";
let len = person.length;
console.log( len );
person = "Mr B";
console.log( person.length );
```

---

## Extracting sub strings

Because strings are just text, they can get quite long. We might want to separate it into parts to be more useful. For instance, what happens if a string contains both the first and family names of someone? Or if a string contains someones date of birth and we need to calculate their age? How can we split it up into parts?

To extract parts of a string we use the `slice()` function after our variable name.

```javascript
let person = "Luke Skywalker";
console.log( person.slice(5) );
console.log( person.slice(5,8) );
console.log( person.slice(0,4) );
```

What are these doing?

* `person.slice(5)` means get from after the 5th character up to the end
* `person.slice(5,8)` means get from after the 5th character up to the 8th character
* `person.slice(0,4)` means get from the beginning, up to the 4th character

The general rule is:

```javascript
let new_string = old_string.slice( after_this_position , up_to_this_position );
```

Another example: What will each of the following print?

```javascript
let s = "To infinity and beyond!";
console.log( s.slice(3,11) );
console.log( s.slice(0,5) );
console.log( s.slice(5) );
console.log( s.slice(-7) );     // what does the negative do?? try it and see!
```

## Searching strings

What if we want Javascript to automatically split a string containing a name into the given name and family name? While the above method will allow us to get parts of a string, we need a way to find where the space is before we can automate it.

To do this, Javascript gives us the `.indexOf()` command. To search for a space, we'd use it like this:

```javascript
let person = "Luke Skywalker";
let space = person.indexOf(" ")
console.log( "The space is located at:",space );
```

What value will be printed from the above?

Notice that it didn't give you the number 5 which is what you might have expected. It actually gives you the number of characters that appear before what you have searched for. (It's actually a bit more technical than that, but not relevant for you at this beginning stage)

Regardless, we now have a numeric variable that tells us the location of the space. We can combine that with the square bracket notation to isolate the parts of the string that contain the given name and family name.

See if this example makes sense:

```javascript
let person = "Luke Skywalker";
let space = person.indexOf(" ");
let given_name = person.slice(0,space);
let family_name = person.slice(space+1);
console.log("Your given name is "+given_name);
console.log("Your family name is "+family_name);
```

## Exercise

* For any string that consists of exactly two words with one space separating them, swap the two words around. For example: If the string `s="Hello world!"`, have the program print `world! Hello`.

---

## Other string functions

Some of the other cool things you can do with strings...

Replacing parts of a string

```javascript
let s = "To infinity and beyond!";
console.log( s.replace(" ", "+") );   // To+infinity+and+beyond!
```

Changing case of text

```javascript
let s = "May the force be with you!";
console.log( s.toLowerCase() );			// may the force be with you!
console.log( s.toUpperCase() );			// MAY THE FORCE BE WITH YOU!
```

Query content of a string

```javascript
let s = "To infinity and beyond!";
console.log( isNaN(s) );       // Returns true if content is Not A Number
```

---