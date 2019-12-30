import time
import math
import pycozmo
from PIL import Image
import ImageTools

def on_cliff_detected(client, state):
    global cozmo    # Bring the cozmo object into this function
    if state:
        print("Cliff detected.")
        # Reverse straight back
        cozmo.drive_wheels(lwheel_speed=-50.0, rwheel_speed=-50.0, duration=1.0)
        # Reversing turn
        cozmo.drive_wheels(lwheel_speed=0.0, rwheel_speed=-50.0, duration=2.8)
        # Drive forward
        cozmo.drive_wheels(lwheel_speed=50.0, rwheel_speed=50.0)

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
# Disconnect from Cozmo
cozmo.disconnect()
cozmo.stop()

