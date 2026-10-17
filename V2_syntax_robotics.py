# syntax check for robotics doc from pybricks V2

from pybricks import version
print(f"Pybricks version: {version}\n")

from pybricks.hubs import ThisHub    
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Color, Direction, Port

DETAILS = False  # print values to see if all is correct. For the error report set DETILS to False

# Needed devices for this test:
# Port.A  -
# Port.B  - motor
# Port.C  - motor
# Port.D  -
# Port.S1 -
# Port.S2 -
# Port.S3 -
# Port.S4 -

# Initialize the EV3
ev3 = ThisHub()

mode = 1  # No idea what it should be.
values = (0, 1, 2, 3, 4)  # Just do something
address = address = 0xD2 >> 1  # shift 1 bit to get a LEGO type of address

if DETAILS:
    for x in dir(ev3):
        if not x.startswith("__"):
            print(f"\t{x}")
    print()

# class DriveBase
# Description: A robotic vehicle with two powered wheels and an optional support wheel or caster.
try:
    from pybricks.pupdevices import Motor
    from pybricks.robotics import DriveBase
    left_motor = Motor(Port.B)
    right_motor = Motor(Port.C)
    wheel_diameter = 30   # milimeters
    axle_track = 120      # milimeters
    distance = 100
    angle = 45
    drive_speed = 50
except Exception as e:
    print(f"\tNot supported: {'robotics':<20} \t{e}\n")
    raise

try:
    dev = DriveBase(left_motor,right_motor,wheel_diameter,axle_track) 
    if DETAILS:
        print(dev.settings())
	# Description: Drives straight for a given distance and then stops.
    dev.settings(straight_speed=500)
    dev.straight(distance)

	# Description: Turns in place by a given angle and then stops.
    dev.turn(angle) 

    val1 = dev.settings()
    if DETAILS:
       print(f"dev.settings: {val1}")
	# Description: Configures the speed and acceleration used by straight() and turn().
    straight_speed,straight_acceleration,turn_rate,turn_acceleration = dev.settings()
    dev.settings(straight_speed,straight_acceleration,turn_rate,turn_acceleration)
    if val1 != dev.settings():
        print(f"DriveBase settings differ after setting \n\t{val1}\n\t{dev.settings()}")

	# Description: Starts driving at the specified speed and turn rate. Both values are measured at the center point between the wheels of the robot.
    dev.drive(drive_speed, turn_rate)

	# Description: Stops the robot by letting the motors spin freely.
    dev.stop() 

	# Description: Gets the estimated driven distance.
    val1 = dev.distance()
    if DETAILS:
        print("dev.distance():", val1)

	# Description: Gets the estimated rotation angle of the drive base.
    val1 = dev.angle() 
    if DETAILS:
        print("dev.angle()", val1)

	# Description: Gets the state of the robot.
    val1 = dev.state()
    if DETAILS:
        print("dev.state()", val1)

	# Description: Resets the estimated driven distance and angle to 0.
    dev.reset() 

	# Description: The traveled distance and drive speed are controlled by a PID controller.
    # You can use this attribute to change its settings.
    # See The Control Class for an overview of available methods.
    val1 = dev.distance_control.limits()
    if DETAILS:
        print(f"dev.distance_control.limits() {val1}")

	# Description: The robot turn angle and turn rate are controlled by a PID controller.
    # You can use this attribute to change its settings.
    # See The Control Class for an overview of available methods.
    val1 = dev.heading_control.target_tolerances()
    if DETAILS:
        print(f"dev.heading_control.target_tolerances() {val1}")
    

	# Description: Stops the robot by letting the motors spin freely.
    dev.stop() 

    wait(500)
except Exception as e:
    print(f"\tNot supported: {'drivebase':<20} \t{e}\n")
    raise

# ── Done ──────────────────────────────────────────────────────
print("\n=== Syntax check complete ===")
