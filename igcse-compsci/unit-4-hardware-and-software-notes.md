# Unit 4 Hardware and software

* 1.3.2 Computer architecture & the fetch-execute cycle
* 1.3.6 Operating systems
* 1.3.7 High & low level languages & their translators 
* 1.3.3 Input devices
* 1.3.4 Output devices
* 1.3.5 Memory, storage devices & media
* 1.1.3 Data storage

## Input devices (1.3.3) and Output devices (1.3.4)



ere's a tip for the devices. Literally I assign each of them a device and they have to become experts in that, then we have a wee EXPO session where others go up and learn about it.

Student produced cheat sheets do in a product of their choice maybe
2/26/20, 11:49 PM - Paul Forbes: *in
2/27/20, 12:30 AM - +86 182 2153 0971: Yes, split them into pairs, assign one input one output to each pair depending on numbers, they have to do 3min-ish talk and produce cheat sheet, which must contain advantages and disadvantages, because goodness knows CIE love that!

---------------------------



Input devices list

* 2D scanner
* 3D scanner
* Bar code reader
* QR code reader
* Digital camera
* Keyboard
* Mouse
* Touch screen (resistive)
* Touch screen (capacitive)
* Interactive whiteboard
* Microphone

You are required to teach your classmates on:

* The principles of operation (how each device works)
   * For example: How does a camera (a) capture an image, (b) convert it into a digital file
   * For example: How does a touch screen (a) detect a finger press, (b) determine where the finger press occurred
   * For example: How does a microphone (a) detect sound waves, (b) convert it into a digital signal
* Include discussion of what sensors are used, and how they function
* Real life scenarios where the devices are used in industry (eg: scanning passports at airport, barcode reader at supermarkets, touch screen information kiosks)
* Compare and contrast the advantages and disadvantages of your device to an alternative (at least 3).

Output devices list

* Inkjet printer
* Laser printer
* 3D printer
* 2D laser cutter
* 3D cutter
* Speakers and headphones
* Actuators
* LCD display
* LED display
* LCD projector
* DLP projector

You are required to teach your classmates on:

* The principles of operation (how the device works)
    * including what are the key components of each device and the role they play in creating the output?
    * including how is the digital signal from the computer converted into the physical output?
* Describe how these are used in real-life scenarios such as industry.
* Compare and contrast the advantages and disadvantages of your device to an alternative.



## Memory, storage devices and media (1.3.5)

* show understanding of the difference between: primary, secondary and off-line storage and provide examples of each, such as: primary: Read Only Memory (ROM) and Random Access Memory (RAM) secondary: hard disk drive (HDD) and Solid State Drive (SSD); off-line: Digital Versatile Disc (DVD), Compact Disc (CD), Blu-ray disc, USB flash memory and removable
HDD
* describe the principles of operation of a range of types of storage device and media including magnetic, optical and solid state
* describe how these principles are applied to currently available storage solutions, such as SSDs, HDDs, USB flash memory, DVDs, CDs and Blu-ray discs
* calculate the storage requirement of a file

## High and low-level languages and their translators (1.3.7)

* high and low level languages
* compilers, interpreters, assemblers
* pi tiein - assemblier, c, c++, python, java

## Operating systems (1.3.6)

purpose; need for interrupts

## Data Storage (1.1.3)

Candidates should be able to:
• show understanding that sound (music), pictures, video, text and numbers are stored in different formats
• identify and describe methods of error detection and correction, such as parity checks, check digits,
checksums and Automatic Repeat reQuests (ARQ)
• show understanding of the concept of Musical Instrument Digital Interface (MIDI) files, JPEG files, MP3 and
MP4 files
• show understanding of the principles of data compression (lossless and lossy) applied to music/video, photos
and text files

### Different storage formats

* Web camera data formats
1920x1080
720
480
8 bit colour depth
24 bit colour depth
Calculate the size of the image (in bytes). Without a calculator, you must show working.

### Error detection and correction

* even and odd parity

### Some common file formats

### Compression

[How Computers Compress Text: Huffman Coding and Huffman Trees - Tom Scott (6:30)](https://www.youtube.com/watch?v=JsTptu56GM8)

* lossy compression
* lossless compression

















* Digital camera https://www.youtube.com/watch?v=B7Dopv6kzJA (5:20m onward)
* Keyboard
* Mouse
* Touch screen (resistive v capacitive) https://www.youtube.com/watch?v=cFvh7qM6LdA



```python
# Create a QR code
# pip install pyqrcode pypng
# pyqrcode library @ https://github.com/mnooner256/pyqrcode
import pyqrcode
qr = pyqrcode.create('https://pbaumgarten.com/')
qr.png("cool website.png", scale=5)
```

```python
# Decode a QR code
# Install zbar as per https://github.com/NaturalHistoryMuseum/pyzbar/#installation
# pip install zbar Pillow ImageToolsMadeEasy
from pyzbar.pyzbar import decode
from PIL import Image
import ImageTools

camera = ImageTools.Camera()
while True:
    input("Press ENTER to take a photo")
    img = camera.take_photo()
    img.show()
    barcodes = decode(img)
    if len(barcodes) > 0:
        print("The following barcodes or qrcodes were found...")
        for i in range(len(barcodes)):
            print(barcodes[i].data.decode())
    else:
        print("No barcode or qrcode")
```

describe how these principles are applied to real-life scenarios, for example: 

* scanning of passports at airports, 
* barcode readers at supermarket checkouts
* touch screens on mobile devices

describe how a range of sensors can be used to input data into a computer system, including:

* light, 
* temperature, 
* magnetic field, 
* gas, 
* pressure, 
* moisture, 
* humidity, 
* pH and 
* motion

describe how these sensors are used in real-life scenarios, for example: 

* street lights, 
* security devices, 
* pollution control, 
* games, and 
* household and industrial applications



## Memory, storage devices and media (1.3.5)

* show understanding of the difference between: primary, secondary and off-line storage and provide examples of each, such as: primary: Read Only Memory (ROM) and Random Access Memory (RAM) secondary: hard disk drive (HDD) and Solid State Drive (SSD); off-line: Digital Versatile Disc (DVD), Compact Disc (CD), Blu-ray disc, USB flash memory and removable
HDD
* describe the principles of operation of a range of types of storage device and media including magnetic, optical and solid state
* describe how these principles are applied to currently available storage solutions, such as SSDs, HDDs, USB flash memory, DVDs, CDs and Blu-ray discs
* calculate the storage requirement of a file

Questions on this have always related to file sizes for this.  As in a picture is 'X' size, how many fit on this thingy 'y'

The midi part I only explain how sound is stored by saying "it's not storing the sound but the calculations, pitch/notelength etc.". Would love to do a little more on this with a midi keyboard for fun.

The jpeg I only keep to "it's a lossy compression" 

MP3 again I don't make too much of a fuss about the actual alogirthms but  little more in-depth about how it 'removes' parts of the sound.  (I use audacity to get them to make some examples)


## High and low-level languages and their translators (1.3.7)

* high and low level languages
* compilers, interpreters, assemblers
* pi tiein - assemblier, c, c++, python, java

## Operating systems (1.3.6)

purpose; need for interrupts

## Data Storage (1.1.3)

Candidates should be able to:
• show understanding that sound (music), pictures, video, text and numbers are stored in different formats
• identify and describe methods of error detection and correction, such as parity checks, check digits,
checksums and Automatic Repeat reQuests (ARQ)
• show understanding of the concept of Musical Instrument Digital Interface (MIDI) files, JPEG files, MP3 and
MP4 files
• show understanding of the principles of data compression (lossless and lossy) applied to music/video, photos
and text files

### Different storage formats

* Web camera data formats
1920x1080
720
480
8 bit colour depth
24 bit colour depth
Calculate the size of the image (in bytes). Without a calculator, you must show working.

### Error detection and correction

* even and odd parity

### Some common file formats

### Compression

[How Computers Compress Text: Huffman Coding and Huffman Trees - Tom Scott (6:30)](https://www.youtube.com/watch?v=JsTptu56GM8)

* lossy compression
* lossless compression
