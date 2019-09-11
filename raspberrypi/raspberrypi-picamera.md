# Raspberry Pi: Using a picamera

## How to use the Picamera to take a photo

The camera is actually quite easy to use in your project. Go ahead and take a selfie or two.

```python
import time
import easyaspi

camera = easyaspi.Camera()
print("I'm going to take a photo! Ready?")
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("Smile!")
camera.photo("selfie.png")
print("All done")
camera.preview(False)               # Close the preview window when done
```

Notice that all we had to do is create the `camera` variable and then use the `.photo()` function? Nice and easy!

There's a couple of other things we can also do with it, like include a message in the image. For example, to add the time and date the photo was taken, add the additional two lines and modify the `camera.photo` line as shown below.

```python
import datetime

now = datetime.datetime.now()
message = now.strftime("%H:%M:%S %d/%m/%Y")
camera.photo("selfie.png", message)
camera.preview(False)               # Close the preview window when done
```

Ready to take it to the next level? Still got your button connected? How about we take a photo when the button is pressed....

```python
import datetime
import time
import easyaspi

BUTTON_PIN = 5
camera = easyaspi.Camera()
button = easyaspi.Button(BUTTON_PIN)

print("Press the button to take a photo")
while not button.get():
    time.sleep(0.1)                 # Wait part of a second and check again
print("SMILE!")
now = datetime.datetime.now()
message = now.strftime("%H:%M:%S %d/%m/%Y")
camera.photo("selfie.png", message)
camera.preview(False)               # Close the preview window when done
```

Can you make the LED blink while we are waiting for the button to be pressed? Check back when we made the button turn on/off when the button was being pressed. How did we make the LED flip, so that when it was off it turned on, and when it was on it turned off. You want to add something similar inside the while loop of this.

## How to use the Picamera to record video

We're not just limited to still photos with the Picamera, we can also record video! (Be aware these video files get very large very quickly. When I was testing it, a few seconds of video were several hundred megabytes each).

To test the video recording function, we could start recording when the program starts, and then stop when the button is pressed.

```python
import time
import easyaspi

BUTTON_PIN = 5
camera = easyaspi.Camera()
button = easyaspi.Button(BUTTON_PIN)

print("Press the button to stop the recording")
camera.record("myvideo.h264")
while not button.get():
    time.sleep(0.1)                 # Wait part of a second and check again
camera.stop()
camera.preview(False)
```

Can you use the LED to indicate that video recording is in progress? It should be quite similar to what you did for the photo exercise.

## Picamera summary

The key parts to using the Picamera are:

* Create the Camera variable

```python
import easyaspi
camera = easyaspi.Camera()
```

* Take a photo (without a message)

```python
camera.photo("myphoto.png")
```

* Take a photo (with a message)

```python
camera.photo("myphoto.png", "my message")
```

* Start video recording

```python
camera.record("myvideo.h264", "my message")
```

* Check to see if camera is recording video

```python
recording_state = camera.recording      # Returns True or False
```

* Stop video recording

```python
camera.stop()
```

* Close the camera preview window when finished

```python
camera.preview(False)
```
