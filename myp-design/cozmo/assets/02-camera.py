import time
import pycozmo
import cv2
import cv2.aruco as aruco
import numpy as np
from datetime import datetime

counter = 0


def on_camera_image(cli, image):
    del cli
    global counter
    counter += 1
    image.save("camera.png", "PNG")
    cv2image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_1000)
    parameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(cv2image, aruco_dict, parameters=parameters)
    print(datetime.now().timestamp(), ids)
    return ids

def on_button_pressed(cli, pkt: pycozmo.protocol_encoder.ButtonPressed):
    del cli
    if pkt.pressed:
        print("Button pressed")
    else:
        print("Button released")        

def pycozmo_program(cli: pycozmo.client.Client):

    angle = (pycozmo.robot.MAX_HEAD_ANGLE.radians - pycozmo.robot.MIN_HEAD_ANGLE.radians) / 2.0
    cli.set_head_angle(angle)

    pkt = pycozmo.protocol_encoder.EnableCamera(enable=True)
    cli.conn.send(pkt)
    pkt = pycozmo.protocol_encoder.EnableColorImages(enable=True)
    cli.conn.send(pkt)
    time.sleep(2.0)
    cli.add_handler(pycozmo.event.EvtNewRawCameraImage, on_camera_image, one_shot=False)

    # Wait for image to stabilize.
    while True:
        time.sleep(2.0)

    # Wait for image to be captured.
    time.sleep(1)


pycozmo.run_program(pycozmo_program)
