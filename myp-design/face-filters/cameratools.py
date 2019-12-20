from PIL import Image, ImageTk
import cv2
import numpy as np

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
        self.min_detect_width = 70
        self.min_detect_height = 70

    def take_photo(self):
        # Read image from the camera
        ret, img = self.cap.read()
        if self.flip:
            img = self.cv2.flip(img, -1)
        # Convert from CV2 image to PIL image
        return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    
    def close(self):
        self.cap.release()
        cv2.destroyAllWindows()

def get_face_in_photo(img, cascade_file):
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
    if len(faces) > 0:
        for (x,y,w,h) in faces:
            face_cv2_img = img[y:y+h,x:x+w]
            # Convert colour photos to PIL color scheme
            face_rgb_img = Image.fromarray(cv2.cvtColor(face_cv2_img, cv2.COLOR_BGR2RGB))
            face_bw_img = Image.fromarray(cv2.cvtColor(face_cv2_img, cv2.COLOR_BGR2GRAY))
            full_rgb_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            return face_rgb_img, face_bw_img, full_rgb_img
    else:
        return None, None, Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

