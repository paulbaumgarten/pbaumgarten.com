import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import os, sys, time, json
import cameratools as ct
import threading
import cv2
import cv2.aruco as aruco

# Pre-define some defaults
FONT_LARGE = ("Arial", 36)
ALLOWED_FILES = (("JPEG files","*.jpg"),("PNG files","*.png"),("all files","*.*"))
CASCADE = "haarcascade_frontalface_default.xml" 

class AppWindow():
    def __init__(self, parent, camera):
        # Create the window
        self.parent = parent
        self.window = tk.Toplevel()
        self.window.geometry("530x420")
        self.window.title("Test app")
        self.window.protocol("WM_DELETE_WINDOW", self.quit)
        self.camera = camera
        self.count = 0
        # Labels
        self.count_label = tk.Label(self.window, text="", font=FONT_LARGE)
        self.count_label.place(x=100,y=20)
        # Button
        self.start = tk.Button(self.window, text="Start photos", command=self.take_photos)
        self.start.place(x=20,y=20)
        self.stop = tk.Button(self.window, text="Stop photos", command=self.stop_photos)
        self.stop.place(x=20,y=60)
        self.start["state"] = "normal"
        self.stop["state"] = "disabled"
        # Create a label reserved for displaying image later
        self.image_label = tk.Label(self.window)
        self.image_label.place(x=20,y=100,width=480,height=270)

    def quit(self):
        self.camera.close()
        self.parent.quit()

    def take_photo(self):
        # Get image selection
        image = self.camera.take_photo()
        # Is there a face in the photo?
        cv2image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_1000)
        parameters = aruco.DetectorParameters_create()
        corners, ids, rejectedImgPoints = aruco.detectMarkers(cv2image, aruco_dict, parameters=parameters)
        # Display the image in the label
        self.tkimg = ImageTk.PhotoImage(image)
        self.image_label.configure(image=self.tkimg)
        if ids is not None:
            # (optional) resize the image
            # Save the files
            print(ids)
            label = ""
            for i in ids:
                label = label + str(i[0])+ " "
            self.count_label.configure(text=label)
        else:
            self.count_label.configure(text="")
        if self.keep_going:
            threading.Timer(1, self.take_photo).start()
            

    def take_photos(self):
        self.keep_going = True
        self.count = 0
        self.start["state"] = "disabled"
        self.stop["state"] = "normal"
        threading.Timer(1, self.take_photo).start()
    
    def stop_photos(self):
        self.start["state"] = "normal"
        self.stop["state"] = "disabled"
        self.keep_going = False

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    camera = ct.Camera(0)
    app = AppWindow(root, camera)
    root.mainloop()
