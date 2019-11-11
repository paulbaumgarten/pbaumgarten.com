# Arduino

The Arduino board is a popular way of controlling with hardware for simple robotics projects or other home made devices/machines. Usually Arduino tutorials would have you use a version of the C++ language, however it is entirely possible to use a Python based approach. Using Python to control an Arduino usually necessiatates the Arduino remaining connected to a PC via the USB cable as the Python program will run on the PC and control the Arduino via USB instead of being loaded onto the Arduino directly. To facilitate this a C++ program is loaded onto the Arduino to interpret the USB commands and executes them on the Arduino.

The following tutorial uses the [Firmata](https://github.com/tino/pyFirmata) module to provide this facility on the Arduino.

```bash
pip install pyfirmata
```

A simple Python program to create a blinking LED on pin 13 would then look like

```python
import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyACM0')

while True:
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)
```

The full tutorial can be found at [realpython.com/arduino-python](https://realpython.com/arduino-python/)

