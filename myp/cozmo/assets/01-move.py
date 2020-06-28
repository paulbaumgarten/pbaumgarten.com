# From https://github.com/zayfod/pycozmo

import pycozmo
import time

lights = [
    pycozmo.lights.red_light,
    pycozmo.lights.green_light,
    pycozmo.lights.blue_light,
    pycozmo.lights.white_light,
    pycozmo.lights.off_light,
]

cli = pycozmo.Client()
cli.start()
cli.connect()
cli.wait_for_robot()

cli.drive_wheels(lwheel_speed=50.0, rwheel_speed=50.0, duration=3.0)
cli.drive_wheels(lwheel_speed=50.0, rwheel_speed=-50.0, duration=1.4)
cli.drive_wheels(lwheel_speed=50.0, rwheel_speed=50.0, duration=3.0)
cli.drive_wheels(lwheel_speed=50.0, rwheel_speed=-50.0, duration=1.4)
cli.drive_wheels(lwheel_speed=50.0, rwheel_speed=50.0, duration=3.0)
cli.drive_wheels(lwheel_speed=50.0, rwheel_speed=-50.0, duration=1.4)
cli.drive_wheels(lwheel_speed=50.0, rwheel_speed=50.0, duration=3.0)
cli.drive_wheels(lwheel_speed=50.0, rwheel_speed=-50.0, duration=1.4)

for light in lights:
    cli.set_all_backpack_lights(light)
    time.sleep(2)

cli.disconnect()
cli.stop()
