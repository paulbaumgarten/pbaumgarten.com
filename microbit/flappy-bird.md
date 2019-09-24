# Flappy bird

```python
# Flappy bird for a micro:bit in python
# http://blog.withcode.uk/2016/05/flappy-bird-microbit-python-tutorial-for-beginners
from microbit import *
import random

display.scroll("Get ready...")

# Game constants
DELAY = 20                      # ms between each frame
FRAMES_PER_WALL_SHIFT = 20      # number of frames between each time a wall moves a pixel to the left
FRAMES_PER_NEW_WALL = 100       # number of frames between each new wall
FRAMES_PER_SCORE = 50           # number of frames between score rising by 1

# Global variables
y = 50
speed = 0
score = 0
frame = 0

# Make an image that represents a pipe to dodge
def make_pipe():
    i = Image("00003:00003:00003:00003:00003")
    gap = random.randint(0,3)   # random wall position
    i.set_pixel(4, gap, 0)      # blast a hole in the pipe
    i.set_pixel(4, gap+1, 0)
    return i
    
# create first pipe
i = make_pipe()

# Game loop
while True:
    frame += 1
    
    # show pipe
    display.show(i)
    
    # flap if button a was pressed
    if button_a.was_pressed():
        speed = -8
        
    # show score if button b was pressed
    if button_b.was_pressed():
        display.scroll("Score:" + str(score))

    # accelerate down to terminal velocity
    speed += 1
    if speed > 2:
        speed = 2
        
    # move bird, but not off the edge
    y += speed
    if y > 99:
        y = 99
    if y < 0:
        y = 0
        
    # draw bird
    led_y = int(y / 20)
    display.set_pixel(1, led_y, 9)
    
    # check for collision
    if i.get_pixel(1, led_y) != 0:
        display.show(Image.SAD)
        sleep(500)
        display.scroll("Score: " + str(score))
        break
    
    # move wall left
    if(frame % FRAMES_PER_WALL_SHIFT == 0):
        i = i.shift_left(1)
    
    # create new wall
    if(frame % FRAMES_PER_NEW_WALL == 0):
        i = make_pipe()
        
    # increase score
    if(frame % FRAMES_PER_SCORE == 0):
        score += 1
    
    # wait 20ms
    sleep(20)   
```

Source: https://blog.withcode.uk/2016/05/flappy-bird-microbit-python-tutorial-for-beginners/9/

