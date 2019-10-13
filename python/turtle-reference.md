# Turtle reference

The following is a summary of turtle instructions, taken from the [Python reference docs](https://docs.python.org/3/library/turtle.html).

## Import

```python
#!/usr/bin/env python3
from turtle import *
```

The turtle will begin in the screen center, facing right. Positive angles rotate counter-clockwise

| Command | Example | Description |
| ------- | ------- | ----------- |
| `home()` | `home()` | return to the starting point and heading |
| `right( angle-in-degrees )` | `right(45)` | Rotate clockwise the given number of degrees |
| `left( angle-in-degrees )` | `left(45)` | Rotate counter-clockwise the given number of degrees |
| `goto( x-coord, y-coord )` | `goto(-50, 50)` | Jump to new x,y coordinates on screen |
| `setx( x-coord )` | `setx(100)` | Jump only the x coordinate to new position |
| `sety( x-coord )` | `sety(100)` | Jump only the y coordinate to new position |
| `setheading( new-angle-in-degrees )` | `setheading(90)` | Point in new direction where 0 == facing right. Positive numbers turn counter-clockwise | 
| `forward( distance )` | `forward(100)` | Move forward given distance of pixels |
| `backward( distance )` | `backward(100)` | Move backward given distance of pixels |
| `circle( radius )` | `circle(50)` | Draw a circle with radius 50 pixels |
| `circle( radius, arc-size-in-degrees )` | `circle(50, 180)` | Draw part of a circle, determined by number of degrees given |
| `dot( radius )` | `dot(50)` | Draw a filled circle(dot) of given size |
| `hideturtle()` | `hideturtle()` | Will still draw but hide the little animated turtle shape. Will speed up complex drawings |
| `showturtle()` | `showturtle()` | Show the turtle when drawing |

## Pen control

| Command | Example | Description |
| ------- | ------- | ----------- |
| `pendown()` | `pendown()` | Draw including whenever moving, jumping location |
| `penup()` | `penup()` | Stop drawing when moving |
| `pensize( width )` | `pensize(1)` | Thickness to draw lines |
| `isdown()` | `isdown()` | Returns True or False based on if the pen is down |

## Get turtle information

| Command | Example | Description |
| ------- | ------- | ----------- |
| `position()` | `x,y = position()` | Returns an (x,y) tuple of the current location |
| `xcor()` | `x = xcor()` | Get the current x-coordinate location |
| `ycor()` | `y = ycor()` | Get the current y-coordinate location |
| `heading()` | `direction = heading()` | Get the current facing direction in degrees |

## Colors

| Command | Example | Description |
| ------- | ------- | ----------- |
| `pencolor( color )` | `pencolor( "yellow") ` | Change the pen color |
| `fillcolor( color )` | `fillcolor( "lime") ` | Change the fill color - see begin_fill() and end_fill()!|
| `begin_fill()` | `begin_fill() ` | Tells Python you are starting a shape you want to be filled in when complete |
| `end_fill()` | `end_fill() ` | Tells Python you have finished the shape and to fill it in |
| `bgcolor( color )` | `bgcolor( "sky blue") ` | Change the background color |
| `bgpic( picture_file )` | `bgpic( "background.gif")` | Set a background picture. Must be GIF format |
| `bgpic( "nopic" )` | `bgpic( "nopic")` | Removes the background picture |

Note: colors can be any of the following:

* A named color, see the list of colour names at [https://trinket.io/docs/colors](https://trinket.io/docs/colors)
* A color code in the in form of "#rrggbb", use the google picker at [https://www.google.com/search?q=color+picker](https://www.google.com/search?q=color+picker)
* A turple of ( red, green, blue ) values from 0 to 255 each

## Screen settings

| Command | Example | Description |
| ------- | ------- | ----------- |
| `screensize( width, height )` | `screensize( 640,480 )` | Set width and height of turtle screen |
| `title( name )` | `title( "My amazing project" )` | Set title name of turtle screen |
| `reset()` | `reset()` | Clear screen, re-center turtle, reset heading to right |
| `clear()` | `clear()` | Clear screen without recentering turtle or resetting heading |
| `window_width()` | `w = window_width()` | Get screen width |
| `window_height()` | `h = window_height()` | Get screen height |
| `isvisible()` | `vis = isvisible()` | Is the turtle visible? |
| `speed( new-speed )` | `speed(10)` | Set drawing speed between 1 and 10. Normally starts at 6. |
| `bye()` | `bye()` | Close turtle |
| `exitonclick()` | `exitonclick()` | Tells Turtle to quit if the exit icon of the screen is clicked |

## Events

| Command | Example | Description |
| ------- | ------- | ----------- |
| `onscreenclick( function )` | `onscreenclick( click )` | execute function when screen clicked. callback must take two parameters for x,y coordinates of the click |
| `onrelease( function )` | `onrelease( click )` | execute function when mouse click let go. callback must take two parameters for x,y coordinates of the click |
| `onkeypress( function, key )` | `onkeypress( pressed, "Up" )` | execute function when nominated key is pressed. callback must take two parameters for x,y coordinates of the click |
| `ontimer( function, time-in-ms )` | `ontimer( ticktock, 1000 )` | execute function once after given number milli-seconds |
| `mainloop()` | `mainloop()` | Start the main event handling loop to run your game |

## Write text to screen

| Command | Example | Description |
| ------- | ------- | ----------- |
| `write( text )` | `write( "Hello there") ` | Write text to screen where ever the turtle is |
| `write( text, font=(fontname,size,weighting)` | `write( "Hello there", font=("Arial",10,"normal")) ` | Write text to screen of specified font |

## Input popup prompts

| Command | Example | Description |
| ------- | ------- | ----------- |
| `textinput("title", "prompt")` | `name = textinput("Name", "What is your name?"` | Popup box for text information |
| `numinput("title", "prompt")` | `num = numinput("Enter a number", "Enter a number between 0 and 100")` | Popup box to enter a number |
