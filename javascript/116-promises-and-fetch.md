# 1.16 - Promises and fetch

Let's introduce the 'promises' method of delayed execution by doing something such as loading interesting content from another website.  We use the `fetch()` function to do this.

```javascript
let url = "https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_joke";
let settings = { mode: 'cors' };

function readJoke( joke ) {
    console.log( joke.setup );
    console.log( "..." );
    console.log( joke.punchline );
}

function receiveJoke( received ) {
    if (received.ok) {
        return received.json();
    }
}

function oops(err) {
    console.log("Something went wrong, hopefully the error message explains it.");
    console.log(err);
}

fetch( url, settings )
    .then(receiveJoke)
    .then(readJoke)
    .catch(oops);
```

Ok, let's try to break this down for you:

* We create three functions, `readJoke()` and `receiveJoke()` and `opps()`.
* `readJoke()` simply accepts a json object as it's parameter, and prints two values from that object to the console. Easy.
* `receiveJoke()` will receive the reply from the website as it's parameter. As part of that reply will be a time consuming `.json()` function. We want `receiveJoke` to call that `.json()` function and return the reply from it, so the joke can ultimately be read to us.
* `fetch()` is where the program starts. We fetch content from the web-address in the `url` parameter and use the settings provided in the json object `settings`. I'll get to all the different settings later. For now, just know we are loading content from the website. You can put that address into your browser and see what it responses with if you wish.
* After `fetch()` has received something, it will ask "what then do I do with this?". That's what the `.then()` function tells it. Once it has received a reply, **then** run the `receiveJoke()` function with the content of the reply.
* Once `receiveJoke()` has finished it's processing (remember it's running that slow .json() function), **then** forward the response from `receiveJoke()` onto the `readJoke()` function.
* Finally, if any errors happen along the way, the `.catch()` will execute the `opps()` function for us.

Whew! It's a bit of a complex thing to get your head around at first. Hopefully it will come with practice, but if not, for now get used to using the above template as a structure for obtaining data from websites.  Let's do a couple of other examples.

```javascript
let url = "https://geocode.xyz/Lausanne?json=1";
let settings = { mode: 'cors' };

function printCityInfo( city ) {
    console.log("Your city, "+city.standard.city+" in "+city.standard.countryname+", is located at longitude "+city.longt+" and latitude "+city.latt);
}

function response( received ) {
    if (received.ok) {
        return received.json();
    }
}

fetch( url, settings )
    .then(response)
    .then(printCityInfo);
```

In this one, the only thing that has changed is the `readJoke()` has been replaced by `printCityInfo()`.

By the way, knowing what the different json object structure looks like (such as, how did I know to call it "city.standard.city") is a case of (1) reading the documentation provided by the website you are getting the information from and (2) looking at sample json data by running the url in the normal browser.

Now, one thing that more experienced programmers will dislike is that I am creating named functions for all these things. I am spelling everything out in more detail like this as I think it makes it easier to understand what is going on when you are learning, but if you were to see an equivilant of the above on stackoverflow or a programmer blog, it would probably look like this:

```javascript
let url = "https://geocode.xyz/Lausanne?json=1";
let settings = { mode: 'cors' };

fetch( url, settings )
    .then(function(received) {
        if (received.ok) {
            return received.json()
        }
    })
    .then(function(info) {
        console.log("Your city, "+info.standard.city+" in "+info.standard.countryname+", is located at longitude "+info.longt+" and latitude "+info.latt);
    });
```

What's going on here is we are now using unnamed or anonymous functions, and coding them straight into the function parameter spaces, rather than passing the function name as a parameter. The workflow is still the same however: fetch() goes and requests a webpage, **then** when it receives a response, it'll run the first `.then()` and the response is provided as the first parameter to the function. When that function finishes it's reply as dictated by the `return` statement is **then** passed as the first parameter to the second `.then()` function as `info`.

Got it? hmmmmm. Let's do one more...

```javascript
let url = "https://api.spacexdata.com/v2/launches/next";
let settings = { mode: 'cors' };

fetch( url, settings )
    .then(function(received) {
        if (received.ok) {
            return received.json()
        }
    })
    .then(function(info) {
        let dt = new Date(Number(info.launch_date_unix)*1000);
        console.log("The next SpaceX mission is "+info.mission_name );
        console.log( "It will launch at "+ dt.toDateString() + " " + dt.toLocaleTimeString() + " (your time)");
        console.log( "The rocket will be a "+ info.rocket.rocket_name );
        console.log( "It will launch from " + info.launch_site.site_name_long );
    })
    .catch(function(err) {
        console.log("Opps... an error!");
        console.log(err);
    });
```

---

## Sending query information

Sometimes you'll have to send additional information with your fetch request, such as an API KEY. An API KEY is simply a passcode issued to you by the website in question (typically you have to sign up with their site to obtain it). You then send this API KEY everytime you are requesting information so they know it is from a valid account. Many websites will allow you to sign up for API KEYs for free. They require the accounts to ensure their systems are not misused/abused by people making 1000s of fetch requests a day.

For an example of this, I've created an account with [http://omdbapi.com/](http://omdbapi.com/).

```javascript
// Our secret key
let apikey = "---get-your-own---"; // sign up to www.omdbapi.com to get your own 

// Ask the user for a movie
let movie = prompt("What movie would you like to know information about?");

// Set up our fetch request
let url = new URL("https://www.omdbapi.com/");
let parameters = {"apikey" : apikey, "t" : movie};
let settings = { "mode": 'cors' };
url.search = new URLSearchParams( parameters );

// Execute our fetch
fetch( url, settings )
    .then(function(received) {
        if (received.ok) {
            return received.json()
        }
    })
    .then(function(info) {
        console.log( "Movie title: " + info.Title );
        console.log( "Year released: " + info.Released );
        console.log( "Rating: " + info.Rated );
        console.log( "Runtime: " + info.Runtime );
        console.log( "Genre: " + info.Genre );
        console.log( "Director: " + info.Director );
        console.log( "Actors: " + info.Actors );
        console.log( "Plot: " + info.Plot );
        console.log( "Box office takings: " + info.BoxOffice );
    })
    .catch(function(err) {
        console.log("Opps... an error!");
        console.log(err);
    });
```

## Exercise: Try one of your own!

The following website lists over a hundred interesting sets of data that are freely available to the public.  Some of them, you will have to sign up for a free account before being able to use their data. If the `Auth` column says `OAuth` it means you will have to login with a Google or Facebook account to access their data. If `Auth` says `apiKey`, it means you sign up to the website and obtain a passcode that you send as part of your fetch request (similar to the previous demo task)

* https://github.com/toddmotto/public-apis

---

## Exercise: Hangman game

Use file functionality to create a simple text-based hangman game!

Source for hangman words: https://raw.githubusercontent.com/Xethron/Hangman/master/words.txt

As a reminder, the following will generate a random number from 0 to 100.

```javascript
let r = Math.random() * 100;
```

To build this exercise, you will need to successfully complete the following:

* Fetch the words list into a Javascript array.
* Use the random number generator to randomly select one item from the list as the secret word
* Reveal the secret word hiding the letters not yet guessed (see below for sample code on this)
* Use a while loop to keep asking the player to guess a new letter
* If a guessed letter is not in the secret word, increase their wrong guesses count and draw the new hangman. (To make it simpler, I suggest that instead of drawing a hangman in the console, you simply print a statement such as `Incorrect guess number 1 of 7` etc)
* If a guessed letter is in the word, add it to your list of correct guesses.

```javascript
// To help you get started, the following function will return a string that can be used to show the length of the secret word and the correct guesses.

function getSecretWordHint( secretWord, lettersGuessed ) {
    let hint = ""
    for (let letter of secretWord) {
        if (lettersGuessed.indexOf(letter) >=0 ) {
            hint = hint + letter;
        } else {
            hint = hint + "_";
        }
    }
    return hint
}

// Example usage

let guesses = ["A","B","C","D","E"];
let hint = getSecretWordHint("SECRET", guesses);
console.log( hint );    // outputs _EC_E_
```

Have fun and good luck!

---
