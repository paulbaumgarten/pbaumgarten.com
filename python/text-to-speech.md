# Speech

## Text to speech

Libraries to install

* gtts (google text to speech)
* playsound (to play the mp3)

```python
from gtts import gTTS
import os
from playsound import playsound

message = input("What do you want me to say?")

# Tex to speech, save as mp3 file
tts = gTTS(text=message, lang='en')
tts.save("hello.mp3")

# Play the mp3 file
playsound("hello.mp3", True)
```

Links

* http://gtts.readthedocs.io/en/latest/index.html
* https://github.com/TaylorSMarks/playsound

## Speech to text

Libraries to install:

* SpeechRecognition
* pyAudio
* google-api-python-client

```python
### File: audiowrapper.py

from threading import Timer
import pyaudio
import wave

class Audio():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100

    def __init__(self):
        self.frames = []
        self.pa = pyaudio.PyAudio()
        self.stream = None

    def __buffer(self, in_data, frame_count, time_info, status):
        self.frames.append(in_data)
        return in_data, pyaudio.paContinue

    def record(self):
        self.frames = []
        self.stream = self.pa.open(format=self.FORMAT,
                                   channels=self.CHANNELS,
                                   rate=self.RATE,
                                   input=True,
                                   frames_per_buffer=self.CHUNK,
                                   stream_callback=self.__buffer)
        self.stream.start_stream()

    def stop(self, filename):
        self.stream.stop_stream()
        self.stream.close()
        self.pa.terminate()
        wf = wave.open(filename, "wb")
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.pa.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def record_and_stop(self, seconds, filename):
        self.record()
        t = Timer(seconds, self.stop, {filename: filename})
        t.start()

    def print_devices(self):
        device_count = self.pa.get_device_count()
        for i in range(0, device_count):
            info = self.pa.get_device_info_by_index(i)
            print("Device {} = {}".format(info["index"], info["name"]))
```

Then in your main file:

```python
import audiowrapper
import speech_recognition as sr

def speech_to_text(filename):
    result = ""
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.record(source)
    try:
        result = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Error: Count not understand audio")
    except sr.RequestError as e:
        print("Error: Request error; {}".format(e))
    finally:
        return result

if __name__ == "__main__":
    audio = audiowrapper.Audio()
    filename = "test.wav"
    s1 = input("Press ENTER to START recording")
    audio.record()
    s2 = input("Press ENTER to STOP recording")
    audio.stop(filename)
    text = speech_to_text(filename)
    print("I think you said: "+text)
```

** Important note **

This is demo code is using an unregistered version of Googles speech recognition system. This only works for a maximum 50 requests per day and they can cancel it for "over use" (even less than the 50). It's only suitable for testing. Google do offer a free one year trial of their full product, but we'd have to sign you up for that. Search for the "google cloud speech api".

Links

* https://pythonspot.com/personal-assistant-jarvis-in-python/
* https://realpython.com/python-speech-recognition/
* https://github.com/Uberi/speech_recognition
* https://people.csail.mit.edu/hubert/pyaudio/ 
* https://cloud.google.com/speech/

