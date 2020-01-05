import time
import pycozmo

movement = False
require_press = True
cli = pycozmo.Client()

def on_camera_image(cli, image):
    del cli
    image.save("camera.png", "PNG")

def on_button_pressed(cli2, pkt: pycozmo.protocol_encoder.ButtonPressed):
    global movement, require_press, cli
    if pkt.pressed:
        movement = not movement
        require_press = False
        print("Button pressed.")
        cli.set_all_backpack_lights(pycozmo.lights.green_light)
        cli.drive_wheels(lwheel_speed=50.0, rwheel_speed=50.0)

def on_robot_picked_up(cli2, state):
    global movement, require_press, cli
    if state: ## state is set to True if picked up
        print("Picked up.")
        require_press = True
        movement = False
        cli.set_all_backpack_lights(pycozmo.lights.red_light)
        cli.drive_wheels(lwheel_speed=0.0, rwheel_speed=0.0)

def on_cliff_detected(cli2, state):
    global movement, require_press, cli
    if state:
        print("Cliff detected.")
        # Reverse
        time.sleep(1)
        cli.set_all_backpack_lights(pycozmo.lights.white_light)
        cli.drive_wheels(lwheel_speed=-50.0, rwheel_speed=-50.0, duration=1.0)
        cli.drive_wheels(lwheel_speed=0.0, rwheel_speed=-50.0, duration=2.8)
        time.sleep(1)
        # Take photo
        angle = (pycozmo.robot.MAX_HEAD_ANGLE.radians - pycozmo.robot.MIN_HEAD_ANGLE.radians) / 2.0
        cli.set_head_angle(angle)
        pkt = pycozmo.protocol_encoder.EnableCamera(enable=True)
        cli.conn.send(pkt)
        pkt = pycozmo.protocol_encoder.EnableColorImages(enable=True)
        cli.conn.send(pkt)
        # Start moving foward again
        cli.set_all_backpack_lights(pycozmo.lights.green_light)
        cli.drive_wheels(lwheel_speed=50.0, rwheel_speed=50.0)

cli.start()
cli.connect()
cli.wait_for_robot()
cli.conn.add_handler(pycozmo.protocol_encoder.ButtonPressed, on_button_pressed)
cli.add_handler(pycozmo.event.EvtRobotPickedUpChange, on_robot_picked_up)
cli.add_handler(pycozmo.event.EvtCliffDetectedChange, on_cliff_detected)
cli.set_all_backpack_lights(pycozmo.lights.blue_light)
while True:
    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        cli.disconnect()
        cli.stop()
        break

