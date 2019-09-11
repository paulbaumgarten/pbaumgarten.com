# 1.14 - Callbacks

Promises and callbacks are technical terms used for a couple of very commonly used tools in the Javascript language. They enable you to write code that will respond to a task when it is completed. That way you your program can carry on doing other things, and then that other code will get executed in the future whenever the conditions you have specified occur.

A very common example we will use in part 2 is to request the web-browser to load a document from a web-server. Because of the nature of the internet, this could take some time (perhaps noticeable seconds), so we don't want our entire program to halt while this happens. Instead, we can write a function that will be automatically executed when the file has loaded, and have it process the content of the file for us.

Another common example is the idea of an "event handler" where we can write code to respond to certain events occuring such as a mouse click on a button.

Callbacks and promises are two different ways that Javascript can achieve this. Callbacks are older way but you will still see them in use a lot. Promises have been built in to Javascript for several years now though as well. It'll be important to be familiar with the basic structure of both.

Let's start by looking at callbacks. One way we might use a call back is through setting up clock timers. Javascript has built in functions for this that work with the concept of callbacks called `setTimeout()` and `setInterval()`. Lets take a look:

The `setInterval()` function below, will call the `tickTock()` function once a second (every 1000 milliseconds)

```javascript
function tickTock() {
    count = count + 1;
    console.log( count + " seconds have lapsed since this started.");
}

let count = 0;
setInterval( tickTock, 1000 );
```

The `setTimeout()` function is slightly different in that it will only execute one instead of continually like the `setInterval()` one.

```javascript
function reply() {
    console.log( "Oh sorry, were you talking to me?" );
}

console.log("Hello are you there?");
setTimeout( reply, 5000 );     // 5 second delay
```

The `setInterval()` can be stopped by saving a value it provides when you start it running and supplying it to `clearInterval()` as shown below.

```javascript
function tickTock() {
    count = count + 1;
    console.log( count + " seconds have lapsed since this started.");
    if (count >= 10) {
        console.log("I'm pretty tired. I think I'll go home now.");
        clearInterval( interval_key );
    }
}

let count = 0;
let interval_key = setInterval( tickTock, 1000 );
```

Exercise: Can you make a program that will act as a count-down timer?  Have it ask the user how many seconds they want to count down, and then give a running countdown until zero at which point it gives an `alert("Times up!");` and then stops the countdown.

---
