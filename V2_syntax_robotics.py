# sytax check for robotics doc from pybricks V2

from pybricks.hubs import ThisHub    
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Color, Direction, Port


# Initialize the EV3
ev3 = ThisHub()

mode = 1  # No idea what it should be.
values = (0, 1, 2, 3, 4)  # Just do something
address = address = 0xD2 >> 1  # shift 1 bit to get a LEGO type of address

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
    print(dev.settings())
    dev.settings(straight_speed=500)
    dev.straight(distance) 
	# Description: Drives straight for a given distance and then stops.

    dev.turn(angle) 
	# Description: Turns in place by a given angle and then stops.

    print(f"dev.settings: {dev.settings()}")
    straight_speed,straight_acceleration,turn_rate,turn_acceleration = dev.settings()
    dev.settings(straight_speed,straight_acceleration,turn_rate,turn_acceleration) 
	# Description: Configures the speed and acceleration used by straight() and turn().

    dev.drive(drive_speed, turn_rate) 
	# Description: Starts driving at the specified speed and turn rate. Both values are measured at the center point between the wheels of the robot.

    dev.stop() 
	# Description: Stops the robot by letting the motors spin freely.

    print(dev.distance())
	# Description: Gets the estimated driven distance.

    print(dev.angle()) 
	# Description: Gets the estimated rotation angle of the drive base.

    print(dev.state()) 
	# Description: Gets the state of the robot.

    dev.reset() 
	# Description: Resets the estimated driven distance and angle to 0.

    print(f"dev.distance_control.limits() {dev.distance_control.limits()}") 
	# Description: The traveled distance and drive speed are controlled by a PID controller.
    # You can use this attribute to change its settings.
    # See The Control Class for an overview of available methods.

    print(f"dev.heading_control.target_tolerances() {dev.heading_control.target_tolerances()}")
	# Description: The robot turn angle and turn rate are controlled by a PID controller.
    # You can use this attribute to change its settings.
    # See The Control Class for an overview of available methods.

    dev.stop() 
	# Description: Stops the robot by letting the motors spin freely.

    wait(500)
except Exception as e:
    print(f"\tNot supported: {'drivebase':<20} \t{e}\n")
    raise
