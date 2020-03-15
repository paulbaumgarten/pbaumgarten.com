# Unit 4 Hardware and software

* 1.3.2 Computer architecture & the fetch-execute cycle
* 1.3.6 Operating systems
* 1.3.7 High & low level languages & their translators 
* 1.3.3 Input devices
* 1.3.4 Output devices
* 1.3.5 Memory, storage devices & media
* 1.1.3 Data storage

## Lesson 1: Computer architecture and the fetch-execute cycle (1.3.2)

"A computer processor does moronically simple things — it moves a byte from memory to register, adds a byte to another byte, moves the result back to memory. The only reason anything substantial gets completed is that these operations occur very quickly. To quote Robert Noyce, ‘After you become reconciled to the nanosecond, computer operations are conceptually fairly simple.’” [*](Code: The Hidden Language of Computer Hardware and Software by Charles Petzold)

Take notes on these two videos to introduce this topic:

* Watch [Tom Scott's exellcent explainer into the Fetch-decode-execute cycle](https://www.youtube.com/watch?v=Z5JC9Ve1sfI) (9:03m).
* Watch [GCSE Computer Architecture 1 - Von Neumann Architecture](https://www.youtube.com/watch?v=ckDb_W72__c) (13:00).

There is an online simulator you can use to experiment with assembler if you are keen:

* [Simple 8-bit Assembler Simulator](http://schweigi.github.io/assembler-simulator/)

Key terms you should be comfortable with:

* Von Neumann model for a computer system
* Control Unit (CU), 
* Arithmetic logic unit (ALU)
* Registers
    * Accumulator (ACC)
    * Program counter (PC)
    * Current instruction register (CIR)
    * Memory address register (MAR) & Memory data register (MDR)
* Random access memory (RAM)
* Bus

Test yourself

* [https://quizlet.com/9917997/test](https://quizlet.com/9917997/test)
* [https://www.bbc.co.uk/bitesize/guides/zbfny4j/test](https://www.bbc.co.uk/bitesize/guides/zbfny4j/test)

## Lesson 2: Computer architecture and the fetch-execute cycle (1.3.2)

... coming

## Lesson 3: Input devices (1.3.3)

GPIO

describe the principles of operation (how each device works) of these input devices

* 2D scanner
* 3D scanner
* Bar code reader
* QR code reader
* Digital camera https://www.youtube.com/watch?v=B7Dopv6kzJA (5:20m onward)
* Keyboard
* Mouse
* Touch screen (resistive v capacitive) https://www.youtube.com/watch?v=cFvh7qM6LdA
* Interactive whiteboard
* Microphone

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

## Output devices (1.3.4)

describe the principles of operation of the following output devices: 

* inkjet, 
* laser and 
* 3D printers; 
* 2D and 3D cutters; 
* speakers and headphones; 
* actuators; 
* flat-panel display screens, such as Liquid Crystal Display (LCD) and Light-Emitting Diodes (LED) display; LCD projectors and Digital Light Projectors (DLP)

describe how these principles are applied to real-life scenarios, for example: 

* printing single items on demand or in large volumes; 
* use of small screens on mobile devices


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
