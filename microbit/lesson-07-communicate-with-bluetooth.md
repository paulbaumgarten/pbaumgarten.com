# Microbit Lesson 7: Bluetooth communication

Today's lesson:

* Using the microbit bluetooth radio

## Video

* [Microbit lesson 7 video](https://youtu.be/w_YkS4abi9U)

## Key points

* Setup

You have to import the radio library, pick a channel number and ensure the radio is turned on. All microbits you want yours to communicate with must be on the same channel (between 0 and 100).

```python
import radio
radio.config(channel=10)
radio.on()
```

* To receive a message

```python
# If there is a message, it will be put into the variable received. Will be set to `None` if there isn't a message.
received = radio.receive()
display.scroll(received)
```

To add a check that there is an actual message first could look like

```python
received = radio.receive()
if received is not None:
    display.scroll(received)
```

* To send a message

```python
radio.send("some message")
```

## Sample program

```python
from microbit import *
import radio

radio.config(channel=10)
radio.on()
while True:
    display.clear()
    if button_a.was_pressed():
        radio.send("iheart")
    if button_b.was_pressed():
        radio.send("upset")
    incoming = radio.receive()
    if incoming == "iheart":
        display.show(Image.HEART)
        sleep(2000)
    elif incoming == "upset":
        display.show(Image.SAD)
        sleep(2000)
    else:
        display.set_pixel(2,2,9)
        sleep(100)
        display.set_pixel(2,2,0)
        sleep(100)
```

## Activity

1. Pair up with another student to create a communicator, inventing your own version of morse code.
2. Pair up with another student to create a small two player game.
3. Pair up with another student, using your Microbit to control the neopixels or music playing on a second Microbit.
4. Pair up with another student, using the accelerometer to tell if the two Microbits are tilting the same way. See if you can match angle without seeing the other microbit.
