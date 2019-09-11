# 1.13 - Functions

Functions are blocks of code that you give a name to that can then be easily run as a whole whenever you need that task performed. They can receive additional information to help with their task, and can return a result containing the information they generate. Writing functions is as if we can create our own Javascript commands that we can then use else where in our programs.

The easiest way to get an idea of functions is through a couple of simple examples. You are probably familiar with the concept of functions in math, so lets return to how we started this entire handbook by doing a little math (only a little I promise).

Hopefully you are comfortable with the following two math formulas:

* Area of a circle: `A = π r^2`
* Circumference of a circle: `C = 2 π r`

Obviously these are fairly simple formula such that you may not bother making functions for them, but it will allow the point to be demonstrated nicely.

```javascript
function area(radius) {
    let area = 2 * Math.PI * radius ** 2;
    return area;
}

function circumference(radius) {
    let circ = 2 * Math.PI * radius;
    return circ;
}

let r = Number(prompt("What is the radius of your circle?"))
let a = area(r);
let c = circumference(r);
console.log("The area of your circle is: ",a);
console.log("The circumference of your circle is: ",c);
```

A few things to point out:

* Function declarations start with the key word `function`. You then give your function a name, followed by any inputs it requires in parenthesis, followed by a set of braces.
* You must have the parenthesis after the function name. If no inputs are required, just leave it empty.
* Just like "if", "while" and "for" you use indenting to show which code belongs to the function.
* The return at the end of the function is optional. If there is no result to pass back to the code that called it, you can skip it.

Functions are very useful for separating common tasks out from your main code. It allows you to avoid repeating yourself all the time which makes your code easier to maintain. Tasks like reading from a file, saving to a file, etc are all ideally suited to being chopped off into a separate function.

Side bar: `You will quickly discover when you start searching sample code online that Javascript, rather confusingly, has at least 6 different syntax for writing functions! This can make things rather confusing for a new programmer looking to understand code you are reading on stackoverflow. For now, I will only use the one method of writing functions in this book and encourage you to practice with that method first. Later in the book as things get more complex it may become more efficient to use an alternative syntax at which point I will (hopefully remember to) discuss the change. If you want to read all about the 6 different syntax, take a look at this good summary https://dmitripavlutin.com/6-ways-to-declare-javascript-functions/`

---

## Optional parameters

The other important thing to appreciate with functions is that you can decide that some parameters are optional, and work with a default value for them if they aren't provided. The following example will make family_name an optional parameter.

```javascript
function greetings( given_name, family_name="" ) {
    if (family_name.length > 0) {
        console.log("Hello "+given_name+" "+family_name)
    } else {
        console.log("Hello "+given_name)
    }
}

// We can provide 1 or 2 parameters to the function

greetings("Jane", "Doe");
greetings("Jane");
```

Functions are very useful things to learn familiarity with. Have a go at making other simple geometry based functions for now such as calculating the surface area or volume of different shapes.

---