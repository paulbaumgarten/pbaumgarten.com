# Snake

```python
# micro:bit tetris by pddring
# source: blog.withcode.uk

from microbit import *

# determines how fast the game is      
FRAME_DELAY = 75
FRAMES_PER_MOVE = 4

# start game animation
smile = Image.HAPPY
sleep(500)
for i in range(9):
  display.show(smile * (i / 9.0))
  sleep(50)
  
# show countdown
display.show("321!")

# define 4 different blocks in 4 different rotations
blocks = [["000:010:000" for i in range(4)],
          ["000:111:000", "010:010:010"] * 2,
          ["011:011:000"] * 4,
          ["010:011:000", "011:010:000", "011:001:000", "001:011:000"]]

# builds up with bricks
clutter = Image("00000:00000:00000:00000:00000")

# get an image of a block
def get_block(type, rot):
  global block_type, rotation, blocks 
  block_type = type % 4
  rotation = rot % 4
  return Image("00000:" + ":".join(["0" + l.replace("1", "9") + "0" for l in blocks[block_type][rotation].split(":")]) + ":00000")

# check if a falling block is about to crash
def about_to_crash(i, screen):
  for y in range(5):
    if y < 4:
      for x in range(5):
        if i.get_pixel(x,y) > 0 and screen.get_pixel(x,y + 1) > 0:
          return True
    else:
      for x in range(5):
        if i.get_pixel(x,y) > 0:
          return True
  return False

# game data
block_type = 0
rotation = 0
y = 5
x = 0
score = 0
frame = 0

# main game loop
while(True):
  b = get_block(block_type, rotation)
  sleep(FRAME_DELAY)
  
  # move left / right
  if button_a.was_pressed():
    x -= 1
  if button_b.was_pressed():
    x += 1
    
  # allow user to move a block multiple times before it falls
  frame += 1
  if frame % FRAMES_PER_MOVE != 0:
    continue
  
  # move brick
  score += 1
  
  if y > 0:
    b = b.shift_up(y)
  else:
    b = b.shift_down(-y)
  if x > 0:
    b = b.shift_right(x)
  else:
    b = b.shift_left(-x)
    
  if x > 2:
    x = 2
  if x < -2:
    x = -2
  y -= 1
  if y < -5:
    y = 5
    block_type += 1
  
  # check if a whole line has been filled
  lines = repr(clutter).replace("Image('","").replace(":')","").split(":")
  for row in range(5):
    if lines[row] == "99999":
      lines.pop(row)
      clutter = Image("00000:" + ":".join(lines))
      break
  
  # check if game is over
  if lines[0] != "00000":
    display.scroll("Score: " + str(score))
    break
  
  # show falling block on top of background
  display.show(b + clutter)
  
  # create new block if one's fallen as far as it can
  if about_to_crash(b, clutter):
    clutter = b + clutter
    y = 5
    block_type += 1
    rotation += 1
    x = 0
  
  # rotate block with accelerometer
  if accelerometer.get_x() < -400:
    rotation -= 1
    
  if accelerometer.get_x() > 400:
    rotation += 1
```

Source: https://blog.withcode.uk/2016/12/microbit-tetris-in-python/
