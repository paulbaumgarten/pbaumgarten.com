# 6 - The HTML Canvas

The HTML canvas is a graphics system that you can program with Javascript. The element is divided into pixels. You use sets of pixel coordinates to tell Javascript where to draw shapes, place text or images etc.

# Coordinate system

Coordinates start with the top-left of the screen being (x=0,y=0).

The x-axis increases as you move to the right.

The y-axis increases as you move down – this is different to the way you do it in Maths so be aware of that!

![Screenshot](img/part-2-coordinate-system.png)

# Hello canvas

HTML:

```html
<canvas id="canvas" width="500" height="500"></canvas>
```  

Javascript:

```javascript
let ctx = document.querySelector("#canvas").getContext("2d");
let w = ctx.canvas.width;
let h = ctx.canvas.height;

// Various properties
ctx.strokeStyle 	= "pink";
ctx.fillStyle 		= "green";
ctx.lineWidth 		= 4;
ctx.font 			= "36pt sans-serif";
ctx.textAlign 		= "left";   // center / right
ctx.textBaseline 	= "bottom"; // middle / top

// Do something
ctx.fillText( "Hello canvas!", 20, 50 );
```



# Drawing basic shapes

Draw a line

```js
ctx.beginPath();
ctx.moveTo(50,50);      // Starting coordinates of the line
ctx.lineTo(450,50);     // Ending coordinates of the line
ctx.stroke();
```

Draw a rectangle

`fillRect( starting-x, starting-y, change-of-x, change-of-y );`   

```js
ctx.clearRect( 10, 100, 480, 50 );
ctx.fillRect( 10, 100, 480, 50 );
ctx.strokeRect( 10, 100, 480, 50 );
```

Draw an ellipse

`ellipse( x-centre, y-centre, x-radius, y-radius, angle-of-rotation, start-angle, end-angle);`   

```js
ctx.beginPath();
ctx.ellipse( 100, 200, 40, 40, 0, 0, 2*Math.PI);
ctx.stroke();
```

Write text

```js
ctx.fillText( message, 250, 20 );
```

# Using colour

```js
ctx.strokeStyle 	= "pink";
ctx.fillStyle 		= "green";
```

# Displaying text

To set the style of your text, there are various attributes you can set in the canvas context:

```js
ctx.font 			= "18pt sans-serif";
ctx.textAlign 		= "left";    // center / right
ctx.textBaseline 	= "bottom";  // middle / top
```

Note: The font must be installed on the **users** computer for it to work. You may want to look at loading an external Google font here [https://github.com/typekit/webfontloader](https://github.com/typekit/webfontloader)

To display text, use the filltext function attached to the context.

```js
ctx.fillText( message, 250, 20 );
```



# Keyboard events


Keyboard codes:

| Key      | Code      | Key      | Code      | Key      | Code      |
|----------|-----------|----------|-----------|----------|-----------|
| Left     | 37        | Up       | 38        | Right    | 39        |
| Down     | 40        | Delete   | 8         | Tab      | 9         |
| Enter    | 13        | Shift    | 16        | Ctrl     | 17        |
| Alt      | 18        | Esc      | 27        | Space    | 32        |

Three main types of keyboard events to listen for:

* The KeyDown event is triggered when the user presses a Key.

```js
document.addEventListener( "keydown", eventHandler );
```

* The KeyUp event is triggered when the user releases a Key.

```js
document.addEventListener( "keyup", eventHandler );
```

* The KeyPress event is triggered when the user presses & releases a Key. (onKeyDown followed by onKeyUp)

```js
document.addEventListener( "keypress", keyPress );
```

The handlers would look at the keyCode property as follows:

```js
function eventHandler(e) {
   let lastKeyPressed = e.keyCode;
}
```

# Mouse events

Add mouse events to an element (eg button)

`document.querySelector("#go").addEventListener("click",addText);` ... or ...     
`document.querySelector("#go").onclick = addText;`

Other useful events: submit, input, change, focus

Add mouse events anywhere in the doc

```js
document.addEventListener("mousemove", moveFunction );
document.addEventListener("click", goFunction );
document.addEventListener("mousedown", downFunction );
document.addEventListener("mouseup", upFunction );
```

Add mouse events to a canvas

```js
ctx.canvas.addEventListener( ...etc );
```

Common properties in the function parameter

```js
e.target.value
e.offsetX // releative to the target element
e.offsetY // releative to the target element
```



# Drawing an image

`canvas.drawImage( imageObject, xposition, yposition, width, height);`   

### Method 1 - Insert an image from your existing HTML, into the canvas

HTML:

```html
<img id="photo" src="http://www.com/path/to/image.jpg" style="display:none">
```

Javascript:

```js
let pic = document.querySelector("#photo");
canvas.drawImage( pic, 50, 200, 150, 150 );
```

### Method 2 - Insert an image from a url source

```js
let pic = new Image();
pic.src = "http://www.com/path/to/image.jpg";
pic.onload = function() {
    canvas.drawImage( pic, 50, 200, 150, 150 );
};
```

# Playing a sound

```js
function soundChomp() {
    let music = document.createElement('audio');
    music.src = "https://pbaumgarten.cs.isl.ch//dist/pacman/pacman_chomp.mp3";
    music.loop = false;
    music.play();
}
```

# Detecting collisions

Unlike the Python Pygame graphhics library, the HTML Canvas does not have any convieniant method of detecting collisions between your shapes drawn. You have to create your own. There is a good explaination of the process and functioning demonstration at:

* [https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection](https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection)

