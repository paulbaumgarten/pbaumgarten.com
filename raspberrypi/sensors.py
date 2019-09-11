#!/usr/bin/env python3
import RPi.GPIO as GPIO
import picamera
import time

GPIO.setmode(GPIO.BCM)

class Ultrasonic():
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def get_distance(self):
        GPIO.output(self.trigger_pin, False)
        time.sleep(0.01)
        GPIO.output(self.trigger_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, False)

        while GPIO.input(self.echo_pin) == 0:
            pulse_start = time.time()

        while GPIO.input(self.echo_pin) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = round(pulse_duration * 17150)
        if distance < 5 or distance > 400:
            return -1
        return distance

class LED():
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.set(False)         # Start with the LED off

    def set(self, power):
        GPIO.output(self.pin, power)

class Button():
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def get(self):
        return GPIO.input(self.pin)

    def on_press(self, callback):
        GPIO.add_event_detect(self.pin, GPIO.RISING, bouncetime=200)
        GPIO.add_event_callback(self.pin, callback)

    def remove_on_press(self):
        GPIO.remove_event_detect(self.pin)

class Camera():
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (1920,1080)
        self.camera.framerate = 15
        self.preview(True)

    def __del__(self):
        self.stop()
        self.camera.stop_preview()
        self.camera.close()

    def preview(self, power):
        if power:
            try:
                self.camera.start_preview(fullscreen=False, window=(0,0,640,480))
                self.camera_on = True
                self.recording = False
                self.camera_ready_time = time.time() + 2 # Camera takes about 2 seconds to start up
            except Exception as e:
                print("PiCamera error: ",str(e))
                self.camera.stop_preview()
                self.camera.close()
        else:
            self.stop()
            self.camera.stop_preview()
            self.camera_on = False

    def photo(self, filename, message=None):
        if self.camera_on:
            while self.camera_ready_time > time.time():
                time.sleep(0.1) # We have to wait until the camera has been on for at least 2 seconds
            if not message == None:
                self.camera.annotate_text = message
                self.camera.annotate_text_size = 36
                self.camera.annotate_background = picamera.Color("black")
                self.camera.annotate_foreground = picamera.Color("white")
            self.camera.capture(filename)
            self.camera.annotate_text = ""
        else:
            raise ValueError("Camera must be on")
            
    def record(self, filename, message=None):    
        if self.camera_on and not self.recording:
            while self.camera_ready_time > time.time():
                time.sleep(0.1) # We have to wait until the camera has been on for at least 2 seconds
            if not message == None:
                self.camera.annotate_text = message
                self.camera.annotate_text_size = 36
                self.camera.annotate_background = picamera.Color("black")
                self.camera.annotate_foreground = picamera.Color("white")
            self.camera.start_recording(filename)
            self.recording = True
        else:
            raise ValueError("Camera must be on")

    def stop(self):
        if self.recording:
            self.camera.stop_recording()
            self.camera.annotate_text = ""
            self.recording = False

    def record_time(self, filename, seconds):
        if self.camera_on:
            self.record(filename)
            self.camera.wait_recording(seconds)
            self.stop()            
        else:
            raise ValueError("Camera must be on")

