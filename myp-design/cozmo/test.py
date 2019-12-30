import time
import math
import pycozmo
from PIL import Image
import ImageTools

def on_cliff_detected(cozmo, state):
    if state:
        print("Cliff detected.")
        # Stop
        cozmo.drive_wheels(lwheel_speed=0.0, rwheel_speed=0.0)

def process_photo(cozmo, image):
    markers = ImageTools.get_aruco(image)
    print(markers)
    # The callback function receives two parameters: the cozmo client object, and a list of integers of markers seen
    if 70 in markers:
        print("I saw ArUco marker 70")
        cozmo.drive_wheels(lwheel_speed=50.0, rwheel_speed=50.0)
    if 71 in markers:
        print("I saw ArUco marker 71")
        cozmo.drive_wheels(lwheel_speed=0.0, rwheel_speed=0.0)
    if 72 in markers:
        print("I saw ArUco marker 72")
        cozmo.drive_wheels(lwheel_speed=50.0, rwheel_speed=-50.0)
        

# Connect to Cozmo
cozmo = pycozmo.Client()
cozmo.start()
cozmo.connect()
cozmo.wait_for_robot()
# Do something simple
cozmo.set_all_backpack_lights(pycozmo.lights.green_light)
time.sleep(1)
cozmo.set_all_backpack_lights(pycozmo.lights.red_light)
time.sleep(1)
cozmo.set_all_backpack_lights(pycozmo.lights.off_light)
cozmo.add_handler(pycozmo.event.EvtCliffDetectedChange, on_cliff_detected)
cozmo.conn.send(pycozmo.protocol_encoder.EnableCamera(enable=True))
cozmo.conn.send(pycozmo.protocol_encoder.EnableColorImages(enable=True))
cozmo.add_handler(pycozmo.event.EvtNewRawCameraImage, process_photo, one_shot=False)

while True:
    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        break
# Disconnect from Cozmo
cozmo.disconnect()
cozmo.stop()

