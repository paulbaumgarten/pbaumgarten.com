<!-- TITLE: Raspberry Pi Setup -->

# Imaging your SD card

Follow the [instructions](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) from the Raspberry Pi website to image your SD card.

When you boot with a fresh install of Raspbian, the default credentials are:

* Username: `pi`
* Password: `raspberry`

# Connect to your network

For home wifi connections this should be fairly straight forward. Click on the wifi icon on the top-right of screen, find your Wifi network and enter your password.

If you are attempting to connect to an Enterprise (managed) network, it can be a bit trickier. The configuration we managed to get working at ISL is [here](setup-enterprisewifi.md).

# Software installation & updates

Open the Raspberry Pi configuration tool (Raspberry Pi menu / Preferences / Raspberry Pi configuration ):

* Enable VNC Server
* Enable SSH Server

Create a file called `requirements.txt` with the following content:

```txt
SpeechRecognition
PyAudio
bs4
youtube_dl
gTTS
google-api-python-client
requests
Wave
pytz
playsound
pafy
```

Open a terminal and run the following:

```bash
# Update and upgrade our system generally
sudo apt update
sudo apt -y upgrade

# Updates needed for PyAudio to install
sudo apt install -y libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
sudo apt install -y python-dev 

# Upgrade PIP to deal with TLS changes
curl https://bootstrap.pypa.io/get-pip.py | sudo python3

# Upgrade setuptools to be compatible with new PIP
sudo pip3 install --upgrade setuptools

# Utilities
sudo apt install -y firefox
sudo apt install -y filezilla
sudo apt install -y vlc-nox
sudo apt install -y vlc

# Audio decoding libraries
sudo apt install -y flac
sudo apt install -y audacity
sudo apt install -y mpg123

# Remove unwanted programs
sudo apt purge -y wolfram-engine
sudo apt purge -y libreoffice*
sudo apt purge -y scratch
sudo apt clean
sudo apt autoremove -y

# Install Python3 dependances
sudo pip3 install -r requirements.txt
sudo pip3 install flask --upgrade

# Upgrade any outdated python packages
# derived from - https://stackoverflow.com/questions/2720014/upgrading-all-packages-with-pip
pip3 list --outdated | cut -d ' ' -f 1 | tail +3 | xargs -n1 sudo pip3 install --upgrade
```

# Setup OpenCV

If you search for documentation on getting OpenCV working on the Raspberry Pi, most articles will talk about needing to compile OpenCV. This is presently **not** necessary. The following procedure is currently working on a Raspberry Pi 3 with Raspbian 2018-06-27. I will update if/when the situation changes. (October 2018)

Open the Raspberry Pi configuration tool (Raspberry Pi menu / Preferences / Raspberry Pi configuration ):

* Enable Pi CAMERA

Open a terminal and work your way through the following commands:

```bash
sudo apt install -y build-essential cmake pkg-config
sudo apt install -y libhdf5-dev libhdf5-serial-dev
sudo apt install -y libqtwebkit4 libqt4-test
sudo apt install -y libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt install -y libxvidcore-dev libx264-dev
sudo apt install -y libgtk2.0-dev libgtk-3-dev
sudo apt install -y libatlas-base-dev gfortran

sudo pip3 install opencv-contrib-python
sudo pip3 install imutils
sudo pip3 install opencv-python
sudo pip3 install "picamera[array]"

# Enable the Raspberry Pi camera to be detected by Open CV
# https://stackoverflow.com/a/37530016
sudo modprobe bcm2835-v4l2 
sudo echo "bcm2835-v4l2" >> /etc/modules
```

Reboot when complete for all changes to take effect

References:

* https://www.pyimagesearch.com/2018/09/19/pip-install-opencv/
* https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/
* https://www.alatortsev.com/2018/04/27/installing-opencv-on-raspberry-pi-3-b/
* https://stackoverflow.com/a/37530016
