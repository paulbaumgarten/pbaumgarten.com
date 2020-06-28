



def take_photo(camera_device_id=0, width=1280, height=720, flip=False ):
    capture_device = cv2.VideoCapture(camera_device_id)
    capture_device.set(3, self.camera_width)
    capture_device.set(4, self.camera_height)
    # Read image from the camera
    ret, img = capture_device.read()
    if flip:
        img = cv2.flip(img, -1)
    # Convert from CV2 image to PIL image
    return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


def detect_faces(img, cascade_file):
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

