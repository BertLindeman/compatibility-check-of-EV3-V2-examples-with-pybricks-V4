
from pybricks import version
print(f"Pybricks version: {version}\n")

from pybricks.hubs import EV3Brick
from pybricks.tools import wait, multitask, run_task
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.nxtdevices import Motor, TouchSensor, ColorSensor, LightSensor, UltrasonicSensor
hub = EV3Brick()

# Needed sensors for this test:
# Port.S1 - NXT touch sensor
# Port.S2 - NXT light sensor
# Port.S3 - NXT color sensor
# Port.S4 - NXT ultrasonic sensor

# define variables used in the doc
color = Color.GREEN  # EV3 only has RED GREEN and ORANGE

ts = TouchSensor(Port.S1)
print(f"TouchSensor is {ts}")
# Some Touch sensors are not detectable, so the define of ts will always succeed
try:
    ts = TouchSensor(Port.S1)
	# Description: LEGO® MINDSTORMS® NXT Touch Sensor.
    wait(500)
	# Description: Checks if the sensor is pressed.
    for i in range(3):
        print(f"ts.pressed() {ts.pressed()}")
        wait(500)
except Exception as e:
    print(f"\tNot supported: TouchSensor \t{e}\n")


# class LightSensor(port)
try:
    ls = LightSensor(Port.S2)
	# Description: LEGO® MINDSTORMS® NXT light Sensor.
    wait(500)
	# Description: Measures the ambient light intensity.
    for i in range(3):
        print(f"{'ls.ambient()':<20} {ls.ambient()}")
        wait(500)
	# Description: Measures the reflection of a surface.
    for i in range(3):
        print(f"{'ls.reflection()':<20} {ls.reflection()}")
        wait(500)
except Exception as e:
    print(f"\tNot supported: LightSensor \t{e}\n")


# class ColorSensor(port)
	# Description: LEGO® MINDSTORMS® NXT Color Sensor.
try:
    cs = ColorSensor(Port.S3)
    
	# Description: Measures the color of a surface.
    for i in range(3):
        print(f"{'cs.color()':<20} {cs.color()}")
        wait(500)
    try:
        # Description: Measures the reflection of a surface with a red, green, blue light.
        for i in range(5):
            print(f"{'cs.rgb()':<20} {cs.rgb()}")
            wait(500)
    
    except Exception as e:
        print(f"\tNot supported: ColorSensor.rgb() \t{e}\n")

    try:
        # Description: Turns on the light at the specified color.
        cs.light.on(color)
        wait(500)
        cs.light.on(Color.BLUE)
        wait(500)
        # Description: Turns off the light.
        cs.light.off()
    
    except Exception as e:
        print(f"\tNot supported: ColorSensor.light.on / off() \t{e}\n")

except Exception as e:
    print(f"\tNot supported: ColorSensor \t{e}\n")


# class UltrasonicSensor(port)
	# Description: LEGO® MINDSTORMS® NXT Ultrasonic Sensor.
try:
    us = UltrasonicSensor(Port.S4)

	# Description: Measures the distance between the sensor and an object using
    # ultrasonic sound waves.
    for i in range(3):
        print(f"{'us.distance()':<20} {us.distance()}")
        wait(500)

except Exception as e:
    print(f"\tNot supported: UltrasonicSensor \t{e}\n")
    raise
