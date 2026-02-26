
"""Test wants motor om Port.A
              touch sensor at Port.S1 or gyro sensor at Port.S1
              Color sensor on Port.S2
              Infrared sensor on Port.S3
              Ultrasonic sensor on Port.S4
"""
from pybricks import version 
from pybricks.hubs import EV3Brick
from pybricks.tools import wait, multitask, run_task
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
hub = EV3Brick()
print(version)
# define variables used in the doc
color = Color.GREEN  # EV3 only has RED GREEN and ORANGE

# class Motor 
try:
    motor = Motor(Port.A, positive_direction=Direction.CLOCKWISE, gears=None)
    # Description: Generic class to control motors with built-in rotation sensors.
    wait(500)
except Exception as e:
    print(f"\tNot supported: motor \t{e}\n")

motor.speed()
    # Description: Gets the speed (angular velocity) of the sensor.

motor.angle()
    # Description: Gets the accumulated angle of the sensor.

angle = 90
motor.reset_angle(angle)
    # Description: Sets the rotation angle of the sensor to a desired value.

motor.stop()
    # Description: Stops the motor and lets it spin freely.

motor.brake()
    # Description: Passively brakes the motor.

motor.hold()
    # Description: Stops the motor and actively holds it at its current angle.
speed = 75
motor.run(speed)
    # Description: Runs the motor at a constant speed.

time = 500
motor.run_time(speed,time,then=Stop.HOLD,wait=True)
    # Description: Runs the motor at a constant speed for a given amount of time.

rotation_angle = 180
motor.run_angle(speed,rotation_angle,then=Stop.HOLD,wait=True)
    # Description: Runs the motor at a constant speed by a given angle.

target_angle = 180
motor.run_target(speed,target_angle,then=Stop.HOLD,wait=True)
    # Description: Runs the motor at a constant speed towards a given target angle.

# motor.run_until_stalled(speed,then=Stop.COAST,duty_limit=None)
#    # Description: Runs the motor at a constant speed until it stalls.

timeout_duration = 250  # in milliseconds

async def run_until_stalled():
    """Coroutine to run the motor until it stalls."""
    await motor.run_until_stalled(speed,then=Stop.COAST,duty_limit=None)

async def timeout_task():
    """Coroutine to enforce a timeout."""
    await wait(timeout_duration)
    await motor.stop(Stop.COAST)  # Stop the motor after the timeout

run_task(multitask((run_until_stalled, timeout_task), race=True))

duty = 25
motor.dc(duty)
    # Description: Rotates the motor at a given duty cycle (also known as “power”).

motor.track_target(target_angle)
    # Description: Tracks a target angle. This is similar to run_target(), 
    # but the usual smooth acceleration is skipped: it will move to the target
    # angle as fast as possible. This method is useful if you want to
    # continuously change the target angle.

# the Control class
print(f"motor.control.scale      {motor.control.scale}")
print(f"motor.control.done()     {motor.control.done()}")
print(f"motor.control.stalled()  {motor.control.stalled()}")
# print current values
print(f"motor.control.limits()  {motor.control.limits()}")
# set limits:
speed = 123
acceleration = 555
actuation = 987
motor.control.limits(speed, acceleration, actuation)

print(f"motor.control.limits()  {motor.control.limits()}")
s, acc, act = motor.control.limits()
assert s == speed, "speed error on limits"
assert acc == acceleration, "accel error on limits"
assert act == actuation, "actuation error on limits"

print(f"motor.control.pid() {motor.control.pid()}")
# V2   doc: pid(kp, ki, kd, integral_range, integral_rate, feed_forward)
# V3.6 doc: pid(kp, ki, kd, integral_deadzone, integral_rate)
try:
    kp,ki,kd,integral_range,integral_rate,feed_forward = motor.control.pid()
    motor.control.pid(kp,ki,kd,integral_range,integral_rate,feed_forward)
except Exception as e:
    print(f"\t motor.control.pid() error: {e}")
    kp,ki,kd,integral_range,integral_rate = motor.control.pid()
    motor.control.pid(kp,ki,kd,integral_range,integral_rate)
# values should be the same or the order is wrong
print(f"check motor.control.pid() {motor.control.pid()}")

#	Description: Gets or sets the PID values for position and speed control.

print(f"motor.control.target_tolerances() {motor.control.target_tolerances()}")
s, p = motor.control.target_tolerances()
motor.control.target_tolerances(s,p)
print(f"motor.control.target_tolerances() {motor.control.target_tolerances()}")
	# Description: Gets or sets the tolerances that say when a maneuver is done.

print(f"motor.control.stall_tolerances() {motor.control.stall_tolerances()}")
s, t = motor.control.stall_tolerances()
print(f"motor.control.stall_tolerances({s},{t}) {motor.control.stall_tolerances(s,t)}")
print(f"motor.control.stall_tolerances() {motor.control.stall_tolerances()}")
	# Description: Gets or sets stalling tolerances.

print(f"motor.stop() {motor.stop()}")  # as theend of the motor section

try:  # see if the touch sensor is on Port S1 
        # class TouchSensor(port)
            # Description: LEGO® MINDSTORMS® EV3 Touch Sensor.
        ts = TouchSensor(Port.S1)
        print(f"ts.pressed() {ts.pressed()}")
            # Description: Checks if the sensor is pressed.
except:
    print("\nNo touch sensor on Port.S1, try Gyro\n")
    # class GyroSensor(port,positive_direction=Direction.CLOCKWISE)
    # Description: LEGO® MINDSTORMS® EV3 Gyro Sensor.
    try:
        gs = GyroSensor(Port.S1)
        print(f"gs.speed() {gs.speed()}")
            # Gets the speed (angular velocity) of the sensor.

        print(f"gs.angle() {gs.angle()}")
            # Gets the accumulated angle of the sensor.
        # If you use the angle() method, 
        # you cannot use the speed() method in the same program. 
        # Doing so would reset the sensor angle to zero every time you read the speed.

        print(f"gs.reset_angle(angle) {gs.reset_angle(angle)}")
            # Sets the rotation angle of the sensor to a desired value.

    except:
        print("\nNo gyro sensor on Port.S1\n")

try:
    # class ColorSensor(port)
        # Description: LEGO® MINDSTORMS® EV3 Color Sensor.
    cs = ColorSensor(Port.S2)
    print(f"cs.color() {cs.color()}")
        # Description: Measures the color of a surface.

    print(f"cs.ambient() {cs.ambient()}")
        # Description: Measures the ambient light intensity.

    print(f"cs.reflection() {cs.reflection()}")
        # Description: Measures the reflection of a surface using a red light.

    print(f"cs.rgb() {cs.rgb()}")
        # Description: Measures the reflection of a surface
        # using a red, green, and then a blue light.

except:
    print("\nNo color sensor on Port.S2\n")

try:
    # class InfraredSensor(port)
    # Description: LEGO® MINDSTORMS® EV3 Infrared Sensor and Beacon.
    ir = InfraredSensor(Port.S3)
    print(f"ir.distance() {ir.distance()}")
        # Description: Measures the relative distance between the sensor and an object using
        # infrared light.

    channel = 1
    print(f"ir.beacon(channel) {ir.beacon(channel)}")
        # Description: Measures the relative distance and angle between the remote and the
        # infrared sensor.

    print(f"ir.buttons(channel) {ir.buttons(channel)}")
        # Description: Checks which buttons on the infrared remote are pressed.

    print(f"ir.keypad() {ir.keypad()}")
        # Description: Checks which buttons on the infrared remote are pressed.

except:
    print("\nNo infrared sensor on Port.S3\n")

try:
    # class UltrasonicSensor(port)
        # Description: LEGO® MINDSTORMS® EV3 Ultrasonic Sensor.
    us = UltrasonicSensor(Port.S4)
    print(f"us.distance(silent=False) {us.distance(silent=False)}")
        # Description: Measures the distance between the sensor and an object using
        # ultrasonic sound waves.

    print(f"us.presence() {us.presence()}")
        # Description: Checks for the presence of other ultrasonic sensors
        # by detecting ultrasonic sounds.
        
    print(f"us.distance(silent=True) {us.distance(silent=True)}")
        # Description: Measures the distance between the sensor and an object using
        # ultrasonic sound waves.
except:
    print("\nNo ultrasonic sensor on Port.S4\n")

print("done on", version)
