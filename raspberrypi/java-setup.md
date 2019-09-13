# Java

## Setup

Raspberry Pi's come with Java pre-installed. If you are using less than version 11, it is recommended you run a distribution upgrade on your Pi.

```bash
sudo apt update
sudo apt dist-upgrade
sudo apt clean
sudo reboot
```

The following will install the pi4j library that Java will use to interface with your Raspberry Pi hardware controls such as the GPIO.

```bash
curl -ssl https://pi4j.com/install | sudo bash
```

If you have any issues with the above command, check the [detailed installation instructions for pi4j](https://pi4j.com/1.2/install.html)

## Install VS Code editor

```bash
wget -o - https://packagecloud.io/headmelted/codebuilds/gpgkey| sudo apt-key add -
sudo apt-get install code-oss=1.29.0-1539702286
apt-mark hold code-oss
```

Instructions sourced from [makeuseof](https://www.makeuseof.com/tag/raspberry-pi-code-oss/)