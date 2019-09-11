# Setup Java (optional)

Raspberry Pi's come with Java pre-installed. If you are using less than version 11, it is recommended you run a distribution upgrade on your Pi.

```bash
sudo apt update
sudo apt dist-upgrade
sudo apt clean
sudo reboot
```

# Setup pi4j

The following will install the pi4j library that Java will use to interface with your Raspberry Pi hardware controls such as the GPIO.

```bash
curl -ssl https://pi4j.com/install | sudo bash
```

If you have any issues with the above command, check the [detailed installation instructions for pi4j](https://pi4j.com/1.2/install.html)

# Example starter activities

* [Control GPIO output such as an LED](https://pi4j.com/1.2/example/control.html)
* [Listen to GPIO input such as a button press](https://pi4j.com/1.2/example/listener.html)

