# Introduction

<img src="img/rpi-logo-web.png" style="float:right">

If you have not previously used or setup your Raspberry Pi before, there are some steps you will need to complete.

* [Setup your Raspberry Pi 3](setup.md)

The default username and password for the Raspberry Pi are as follows:

* Username: pi
* Password: raspberry

It is important to keep a reference of the Raspberry Pi pin numbering, as the numbers are not in any meaningful sequence. Refer to the following diagram for the Raspberry Pi 3(b).

![](img/raspberry-pi-3-pinout.jpg)

**Power supply warning** - The Pi will automatically turn itself on when you plug the power in. The Pi draws power through its micro USB port. You need a power supply of at least 2500 mA (be aware most phone chargers only provide 1500 to 2000 mA). The Pi will sometimes "appear" to work with a less capable power supply but will sometimes behave in weird unexplained ways if you aren't giving it enough power.

# Programming with Python

* [Using LEDs](gpio-led.md)
* [Using Buttons](gpio-button.md)
* [Using Ultrasonic sensors](gpio-ultrasonic.md)
* [Using PiCamera](picamera.md)
* [Using the GPIO without easyaspi](gpio.md)

# Programminng with Java

* [Get setup for Java on the Raspberry Pi](java-setup.md)
* [Basic examples for GPIO](java-gpio.md)
* [Official JavaDocs for Pi4J](https://pi4j.com/1.2/apidocs/index.html?com/pi4j/io/gpio/GpioFactory.html)  (external)
* [Control GPIO output such as an LED](https://pi4j.com/1.2/example/control.html) (external)
* [Listen to GPIO input such as a button press](https://pi4j.com/1.2/example/listener.html)  (external)

# Programming with Assembler

For those who want the red pill...

* http://www.science.smith.edu/dftwiki/index.php/Tutorial:_Assembly_Language_with_the_Raspberry_Pi#Blinking_LED
* https://thinkingeek.com/arm-assembler-raspberry-pi/

# Project ideas

* [Your first challenge exercises](challenges.md)
* [Hackster projects](https://www.hackster.io/projects/tags/python)
* [Infrared IR blaster using lirc](project-lirc.md)
* [Coin acceptor](project-coin-acceptor.md)

# System management guides

* [Useful terminal commands for Raspberry Pi](terminal-commands.md)
* [System services](services.md) - How to setup a project to start on bootup and run in the background
* [Using environment variables for credentials/api keys](key-handling.md)

Refer to my [sysadmin repo](https://github.com/paulbaumgarten/sysadmin-notes/) for more information

# Official documentation links

* [GPIO documentation](https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/)
* [Pi Camera documentation](https://picamera.readthedocs.io/en/release-1.13/)
* [Pillow (Python Imaging Library) documentation](https://pillow.readthedocs.io/en/stable/)
* [Open CV documentation](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)

