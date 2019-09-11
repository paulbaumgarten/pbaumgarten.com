# Book of Javascript

<img src="img/js-logo.png" style="float:right">

## Chapter 1 - Javascript basics

Quicklinks to Repl language playgrounds: 

* [Javascript](https://repl.it/languages/javascript)
* [HTML/CSS/JS](https://repl.it/languages/html)

Lessons

* 1.0 - [Introduction & getting Javascript up and running](100-intro.md)
* 1.1 - [Numeric calculations](101-numbers.md)
* 1.2 - [Numeric variables](102-numeric-variables.md)
* 1.3 - [String variables](103-strings.md)
* 1.4 - [User input](104-ui.md)
* 1.5 - [Converting between numbers and strings](105-casting.md)
* 1.6 - [Comparing values](106-comparing.md)
* 1.7 - [Making decisions with "if"](107-if.md)
* 1.8 - [Repeating instructions with "while"](108-while.md)
* 1.9 - [Making a list](109-arrays.md)
* 1.10 - [Looping through a list](110-looping-arrays.md)
* 1.11 - [Other list functionality](111-array-functions.md)
* 1.12 - [Dates and times](112-dates-times.md)
* 1.13 - [Functions](113-functions.md)
* 1.14 - [Callbacks](114-callbacks.md)
* 1.15 - [JSON](115-json.md)
* 1.16 - [Promises and using fetch](116-promises-and-fetch.md)
* 1.17 - [Classes](117-classes.md)

# Chapter 2 - HTML

* 2.1 - Introduction to HTML
* 2.2 - A tags
* 2.3 - DIV, SPAN tags
* 2.4 - IMG, VIDEO, AUDIO tags
* 2.5 - FORM tags
* 2.6 - Lists
* 2.7 - Tables

# Chapter 3 - CSS

* 3.1 - Selectors
* 3.2 - Boiler plate
* 3.3 - Basic styling
* 3.4 - Showing/hiding items
* 3.5 - Grid layout
* 3.6 - Drop down menus
* 3.7 - Styling form elements
* 3.8 - Icons
* 3.9 - Styling tables

# Chapter 4 - Javascript exercises with HTML & CSS

* 4.1 - Document object model functions & properties
* 4.2 - Event handlers
* 4.3 - Basic form tasks (validation, send)
* 4.4 - Uploading files
* 4.5 - Local storage

# Chapter 5 - Firebase

* 5.1 - Firebase authentication - see [online demo](htps://authdemo.jigsawapps.net/)
* 5.2 - Firebase database - see [online demo](htps://notekeeper.jigsawapps.net/)
* 5.3 - Firebase file storage - see [online demo](htps://notekeeper.jigsawapps.net/)

Appendum: Use the following firebase database rules

```json
{
  /* Visit https://firebase.google.com/docs/database/security to learn more about security rules. */
  "rules": {
    ".read": "auth != null",
    ".write": "auth != null"
  }
}
```

# Chapter 6 - Canvas

* 6.1 - Coordinate system
* 6.2 - Hello canvas!
* 6.3 - Drawing basic shapes
* 6.4 - Using colour
* 6.5 - Displaying text
* 6.6 - Keyboard events
* 6.7 - Mouse events
* 6.8 - Drawing an image
* 6.9 - Playing a sound
* 6.10 - Detecting collisions

# Additional content

Not everything made it into the first edition of book that probably should have.

* [Reading an uploaded file in the browser](javascript-read-uploaded-file-in-broswer)
* [Geolocation](javascript-geolocation)
* [Detect screen size, device type](javascript-detect-device)
* [Cordova](javascript-cordova)

# Reference guides & valuable links

Some summary guides that might be useful.

* [My Javascript reference summary](/javascript-notebook) (also available as [PDF](/uploads/javascript/javascript-notebook.pdf))
* [HTML 5](/uploads/javascript/javascript-cheatsheet-html.pdf "Javascript Cheatsheet HTML")
* [HTML Canvas](/uploads/javascript/javascript-cheatsheet-canvas.pdf "Javascript Cheatsheet Canvas")
* [CSS 3](/uploads/javascript/javascript-cheatsheet-css.pdf "Javascript Cheatsheet CSS")

Official documentation from the Mozilla developer network

* [Mozilla developer network: Javascript documentation](https://developer.mozilla.org/bm/docs/Web/JavaScript)
* [Mozilla developer network: HTML documentation](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [Mozilla developer network: CSS documentation](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Mozilla developer network: Web API documentation](https://developer.mozilla.org/en-US/docs/Web/API)

Get copies of the MDN documents offline:

* http://devdocs.io/offline

For thorough, free, high quality references to other languages, I highly recommend the Notes for Professionals series of PDFs available from [goalkicker](https://goalkicker.com):

* [Javascript notes for professionals](https://goalkicker.com/JavaScriptBook/)
* [CSS notes for professionals](https://goalkicker.com/CSSBook/)
* [HTML 5 notes for professionals](https://goalkicker.com/HTML5Book/)
* [HTML 5 Canvas notes for professionals](https://goalkicker.com/HTML5CanvasBook/)

Programming practice

* [CodingBat for Javascript](https://codingjs.pbaumgarten.com/)

Project ideas

* ["I Need Practice Programming": 49 Ideas for Game Clones to Code](http://inventwithpython.com/blog/2012/02/20/i-need-practice-programming-49-ideas-for-game-clones-to-code/) or [PDF](/uploads/python/python-blog-49-ideas.pdf)
* [Juice it or lose it](https://www.youtube.com/watch?v=Fy0aCDmgnxg) (a talk by Martin Jonasson & Petri Purho)

Javascript Games: A youtube series that looks quite good:

* [Javascript Games series: Pong](https://www.youtube.com/watch?v=nl0KXCa5pJk&index=2&list=PLt4757glfbhHkfz7dqojMbnBdgUnFih4B)
* [Javascript Games series: Flappy bird](https://www.youtube.com/watch?v=L07i4g-zhDA&index=3&list=PLt4757glfbhHkfz7dqojMbnBdgUnFih4B&t=0s)
* [Javascript Games series: Snake](https://www.youtube.com/watch?v=9TcU2C1AACw&index=4&list=PLt4757glfbhHkfz7dqojMbnBdgUnFih4B&t=0s)
* [Javascript Games series: Tetris](https://www.youtube.com/watch?v=HEsAr2Yt2do&index=5&list=PLt4757glfbhHkfz7dqojMbnBdgUnFih4B&t=0s)
