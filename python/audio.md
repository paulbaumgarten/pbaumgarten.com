# Audio

A guide to some of the most common ways of working with audio in Python.

## Install libraries

### Pyaudio

#### Windows

```bash
pip install pyaudio
```

#### Mac OSX

```bash
# portaudio is a required pre-requisite on the mac
brew install portaudio
pip3 install pyaudio
```

#### Linux / Raspberry Pi

```bash
sudo apt-get install python-pyaudio python3-pyaudio
```

* From http://people.csail.mit.edu/hubert/pyaudio/#Installation


## List of audio devices

```python
def list_devices():
    p = pyaudio.PyAudio()
    device_count = p.get_device_count()
    for i in range(0, device_count):
        info = p.get_device_info_by_index(i)
        print("Device {} = {}".format(info["index"], info["name"]))
```

## Record from microphone, process live.

```python
import pyaudio
import wave
import sys

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
DEVICE = 0 # use list_devices() to determine

# instantiate PyAudio
p = pyaudio.PyAudio()

# open stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                frames_per_buffer=CHUNK,
                input=True,
                input_device_index=DEVICE,
                output=False) 
                # output flag: do you want the audio to playback over speaker? Be wary of audio feedback if you set to True.

# read data
data = wf.readframes(CHUNK)

# play stream
record = True
while record:
    data = stream.read(CHUNK)
    ### TO DO:
    ### Insert your audio processing logic here
    ###
    record = False # At some point stop your recording!

# stop stream
stream.stop_stream()
stream.close()

# close PyAudio
p.terminate()
```

## Record from microphone, save to sound file

```python
import pyaudio
import wave
import sys

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
TARGET_FILE = "filename.wav" # Change as required
DEVICE = 0 # use list_devices() to determine

# instantiate PyAudio
p = pyaudio.PyAudio()

# open stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                frames_per_buffer=CHUNK,
                input_device_index=DEVICE,
                input=True,
                output=False) 
                # output flag: do you want the audio to playback over speaker? Be wary of audio feedback if you set to True.

# read data
data = wf.readframes(CHUNK)

# process stream
save_data = []
record = True
while record:
    data = stream.read(CHUNK)
    save_data.append(data)
    ### TO DO:
    ### Insert your audio processing logic here
    ###
    record = False # At some point stop your recording!

# stop stream
stream.stop_stream()
stream.close()

# close PyAudio
p.terminate()

# save to file
wf = wave.open(TARGET_FILE, "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(save_data))
wf.close()
```

## Play audio file

## Analyse audio from an existing recording

```python
import pyaudio
import wave
import sys

CHUNK = 1024

SOURCE_FILE = "filename.wav" # Change as required

# Open WAV file
wf = wave.open(SOURCE_FILE, 'rb')

# instantiate PyAudio
p = pyaudio.PyAudio()

# open audio stream
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# read data
data = wf.readframes(CHUNK)

# play stream
while len(data) > 0:
    stream.write(data)
    data = wf.readframes(CHUNK)
    ### TO DO:
    ### Insert your audio processing logic here
    ###

# stop stream
stream.stop_stream()
stream.close()

# close PyAudio
p.terminate()
```


## Detect amplitude

Requires `numpy` library.

* Install with `pip install numpy`
* Import with `import numpy`

```python
def get_amplitude_from_stream(data_stream):
    # Convert to numpy array
    # Switched from fromstring to frombuffer thanks to https://stackoverflow.com/questions/24974032/reading-realtime-audio-data-into-numpy-array
    narr = numpy.frombuffer(data_stream, dtype=numpy.int16)
    # Convert numpy arra from int16 to int32 for error free calculations when squaring
    narr = narr.astype(numpy.int32, copy=False)
    # Calculate the rootMeanSquare of the samples
    # https://en.wikipedia.org/wiki/Amplitude#Root_mean_square_amplitude
    rootMeanSquare = numpy.sqrt(numpy.mean(narr**2))
    if rootMeanSquare > 0:
        # Convert root mean square of raw power to a decibel scale
        decibel = 20 * math.log10(rootMeanSquare)
    else:
        decibel = 0
    return decibel
    # end of function
```

Based on [source](https://stackoverflow.com/questions/51431859/how-do-i-get-the-frequency-and-amplitude-of-audio-thats-being-recorded-in-pytho)


## Detect frequency &/or pitch

I have done this successfully guided a student through this process before just using numpy. Code that worked in 2018 is as follows...

* Install with `pip install numpy`
* Import with `import numpy`

```python
import numpy as np

def bytes_array_to_hex_string( input ):
    return "".join(format(x, "02x") for x in input)

def get_frequency_from_stream(data_stream):
    numpydata = np.fromstring(data_stream, dtype=np.int16)
    w = np.fft.fft(numpydata)
    freqs = np.fft.fftfreq(len(w))
    idx = np.argmax(np.abs(w))
    freq = freqs[idx]
    freq_in_hertz = abs(freq * RATE)
    return freq_in_hertz

def determine_note(freq):
    # From https://pages.mtu.edu/~suits/notefreqs.html
    if freq >= 654.3 and freq <= 664.3:
        note = "E5"
    if freq >= 435.0 and freq <= 445.0:
        note = "A4"
    if freq >= 288.7 and freq <= 298.7:
        note = "D4"
    if freq >= 191.0 and freq <= 201.0:
        note = "G3"
    if freq >= 386.9 and freq <= 396.9 :
        note = "G4"
    if freq >= 324.6 and freq <= 334.6:
        note = "E4"
    if freq >= 344.2 and freq <= 354.2:
        note = "F4"
    if freq >= 488.9 and freq <= 498.9:
        note = "B4"
    if freq >= 256.6 and freq <= 266.6:
        note = "C4"
    return(note)
```

**Alternative advice from StackOverflow**

**Detecting frequency**

Commonly used in DSP, the frequency spectrum can be analyzed using the [DFT](https://en.wikipedia.org/wiki/Discrete_Fourier_transform) (Discrete Fourier Transform). You will usually see this under the name FFT (Fast Fourier Transform), since this is the most popular implementation of the DFT. There are already Python libraries that implement the FFT for you and are simple to use.

Please note that this will give you an array the length of your block size that contains complex information (real signal + phase information) i.e. the frequency information. This does not mean you can necessarily identify the pitch of incoming audio (you can't directly tell that someone is playing an A1 note on the piano, unless the signal is really high quality and you still have some basic DSP processing as well as the FFT).

For reference:

* Here is a link to the [scipy.fft](https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html) and how to get started
* And here is the link for [numpy.fft](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.fft.fft.html#numpy.fft.fft) with a couple of examples

You can call this function in your processing loop if you wanted to do something with the frequency information.

**Detecting pitch (musical note)**

This is a non-trivial task that many people try to accomplish. Most algorithm's usually involve the FFT (as discussed before), but have another layer of complicated processing on top. I would recommend using a library unless you fancy developing your own algorithm:

* [Google's REAPER](https://github.com/google/REAPER) algorithm (would need to be [wrapped into Python](https://stackoverflow.com/questions/1942298/wrapping-a-c-library-in-python-c-cython-or-ctypes))
* [Aubio](https://github.com/aubio/aubio) Python DSP library
* [Librosa](https://librosa.github.io/librosa/) Python audio analysis library (here's an [example](https://github.com/tyrhus/pitch-detection-librosa-python/blob/master/script_final.py) to get started)

[Source](https://stackoverflow.com/questions/51431859/how-do-i-get-the-frequency-and-amplitude-of-audio-thats-being-recorded-in-pytho)

## References

* http://people.csail.mit.edu/hubert/pyaudio/
* https://stackoverflow.com/questions/51431859/how-do-i-get-the-frequency-and-amplitude-of-audio-thats-being-recorded-in-pytho

