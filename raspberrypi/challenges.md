# Raspberry Pi challenges

# Challenges

Now you've learnt the core bits of the Raspberry Pi, it's time to put them to use. Your `sensors.py` file is now complete. You only need to modify your main project file now.

Here are some ideas for potential mini-projects you might like to try:

## Challenge 1: Motion sensor alarm that takes a photo of the intruder

You will need your Ultrasonic sensor and Camera for this to work. Use the camera to take a photo anytime someone comes within a meter of your Raspberry Pi! For this to be useful, you'll want to change the name of the PNG file each time so you don't just save over the top of the same file.

As a suggestion, I'd use a filename based on the current time and date. Perhaps using something like this? Make sure you include a time/date stamp annotation in the PNG file as well.

```python
now = datetime.datetime.now()
filename = now.strftime("%Y-%m-%d-%H-%M-%S.png")
```

## Challenge 2: Motion sensor alarm that records video of the intruder

Modify the previous challenge so that it records the intruder on film!

* Start recording when the intruder comes within a meter of the Raspbery Pi
* Stop recording once the intruder has gone away
* Keep looping, so if they return, you record them again

## Challenge 3: Add some LEDs and Buttons to your intruder alarm

Modify either of the previous challenges (ie: use photos or video, whichever you prefer) to incorporate a few extra features:

* One LED that indicates the program is running... watching... guarding
* A second LED that indicates the alarm has been triggerd
* A button to end the program loop

## Challenge 4: Make a selfie-studio

Moving away from the intruder detection system, here's a different idea using 2 buttons, 2 LEDs and the camera.

* One button used to take a photo when pressed
* A second button used to start/stop a video when pressed
* Keep looping so you can take as many photos and videos as you like
* One LED to indicate video recording in progress
* Another LED to indicate photo is being taken
