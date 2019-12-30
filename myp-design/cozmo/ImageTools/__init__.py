from PIL import Image, ImageTk
import cv2
import numpy as np
import os

MIN_DETECT_WIDTH = 100
MIN_DETECT_HEIGHT = 100

def convert_cv2_to_pil( cv2_image ):
    pil_image = Image.fromarray(cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB))
    return pil_image

def convert_pil_to_cv2( pil_image ):
    cv2_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    return cv2_image

class Camera():
    def __init__(self, camera_device_id=0, width=1280, height=720, flip=False ):
        self.camera_device_id=camera_device_id
        self.flip = flip
        self.camera_width = 1280
        self.camera_height = 720
        self.cap = cv2.VideoCapture(self.camera_device_id)
        self.cap.set(3, self.camera_width)
        self.cap.set(4, self.camera_height)

    def record_video(self, length=0.0, filename="", per_frame_callback=None, preview=False ):
        pass

    def record_video_stop(self):
        pass

    def take_photo(self, preview=False):
        # Read image from the camera
        ret, img = self.cap.read()
        if self.flip:
            img = cv2.flip(img, -1)
        if preview:
            cv2.imshow(img)
        # Convert from CV2 image to PIL image
        return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    
    def close(self):
        self.cap.release()
        cv2.destroyAllWindows()

def get_faces(img, cascade_file):
    if not os.path.exists(cascade_file):
        raise Exception("[get_faces] Cascade file does not exist")
    if not isinstance(img, Image.Image):
        raise Exception("[get_faces] Not a PIL.Image.Image object")
    # Convert from PIL image to CV2 image
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    # Returns the colour of face, grayscale of face, and full image containing face if there is a face in the photo
    cascade = cv2.CascadeClassifier(cascade_file)
    # Convert image to grey scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect any faces in the image? Put in an array
    faces = cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(MIN_DETECT_WIDTH, MIN_DETECT_HEIGHT)
    )
    # If there is a face
    return faces

def get_object_crop(img, obj_coordinates):
    if not isinstance(img, Image.Image):
        raise Exception("[get_object_crop] Not a PIL.Image.Image object")
    # obj_coordinates should be a tuple of (x,y,w,h)
    x,y,w,h = obj_coordinates
    return img.crop((x,y,x+w,y+h)) # left, top, right, bottom

def get_object_crops_multi(img, list_obj_cordinates):
    if not isinstance(img, Image.Image):
        raise Exception("[get_object_crops_multi] Not a PIL.Image.Image object")
    crops_list = []
    if len(list_obj_cordinates) > 0:
        for (x,y,w,h) in list_obj_cordinates:
            img2 = img.crop((x,y,x+w,y+h)) # left, top, right, bottom
            crops_list.append(img2)
        return crops_list
    else:
        return None

def get_aruco(img):
    import cv2
    import cv2.aruco as aruco
    if not isinstance(img, Image.Image):
        raise Exception("[get_aruco] Not a PIL.Image.Image object")
    # Use OpenCV to detect any possible aruco markers in our image
    cv2image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_1000)
    parameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(cv2image, aruco_dict, parameters=parameters)
    # If we recognised an aruco marker
    aruco_codes = []
    if ids is not None:
        # For some reason the ids are a list of lists, eg [[37], [14]]. Change that into [37, 14]....
        for sublist in ids:
            if len(sublist) > 0:
                aruco_codes.append(sublist[0])
    return aruco_codes
