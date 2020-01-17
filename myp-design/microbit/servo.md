# Controlling Servos with Microbit

![](img/servo.JPG)

Tested on the micro servo 9g

Servo control: 

* 100 = 1 millisecond pulse all right 
* 200 = 2 millisecond pulse all left 
* 150 = 1.5 millisecond pulse center 
* 600 * 0.0512 = clockwise
* 1800 * 0.0512 = anticlockwise

Demo code...

```python
from microbit import * 

# configure analog writing for pin0
pin0.set_analog_period(20)

while True: 
    # rotate to 0 degrees on micro servo 9g at 3.3v
    pin0.write_analog(10) 
    sleep(1000)

    # rotate to 180 degrees on micro servo 9g at 3.3v
    pin0.write_analog(120)
    sleep(1000)

    # no rotation
    pin0.write_analog(0)
    sleep(1000)
```

Derived from https://support.microbit.org/support/solutions/articles/19000101864-using-a-servo-with-the-micro-bit
