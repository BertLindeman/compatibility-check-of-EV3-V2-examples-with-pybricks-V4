
"""Test wants motor om Port.A
            EV3 touch sensor      on Port.S1 or gyro sensor
            EV3 Color sensor      on Port.S2
            EV3 Infrared sensor   on Port.S3
            EV3 Ultrasonic sensor on Port.S4
"""

from pybricks import version
print(f"Pybricks version: {version}\n")

# from pybricks.hubs import EV3Brick
from pybricks.tools import wait, multitask, run_task
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor

from uerrno import ENODEV, ETIMEDOUT

# hub = EV3Brick()

# define variables used in the doc
color = Color.GREEN  # EV3 only has RED GREEN and ORANGE

NODEV = (ENODEV, ETIMEDOUT)
err_count = 0
DETAILS = False  # True

# class Motor
try:
    motor = Motor(Port.A, positive_direction=Direction.CLOCKWISE, gears=None)
    # Description: Generic class to control motors with built-in rotation sensors.
    wait(500)
except Exception as ex:
    if ex.args[0] in NODEV:
        err_count += 1
        print("No motor attached at Port.A")
    else:
        err_count += 1
        print(f"\tNot supported: motor \t{ex}\n")
else:
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
    # Description: Runs the motor at a constant speed for a given amount of time.
    motor.run_time(speed,time,then=Stop.HOLD,wait=True)

    rotation_angle = 180
    # Description: Runs the motor at a constant speed by a given angle.
    motor.run_angle(speed,rotation_angle,then=Stop.HOLD,wait=True)

    target_angle = 180
    # Description: Runs the motor at a constant speed towards a given target angle.
    motor.run_target(speed,target_angle,then=Stop.HOLD,wait=True)

    # Description: Runs the motor at a constant speed until it stalls.
    # motor.run_until_stalled(speed,then=Stop.COAST,duty_limit=None) In function later

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
    scale = motor.control.scale
    done = motor.control.done()
    stalled = motor.control.stalled()
    limits1 = motor.control.limits()
    if DETAILS:
        print(f"motor.control.scale      {scale}")
        print(f"motor.control.done()     {done}")
        print(f"motor.control.stalled()  {stalled}")
        # print current values
        print(f"motor.control.limits()  {limits1}")
    # set limits:
    speed = 123
    acceleration = 555
    actuation = 987
    motor.control.limits(speed, acceleration, actuation)
    limits2 = motor.control.limits()

    if DETAILS:
        print(f"motor.control.limits()  {motor.control.limits()}")
    s, acc, act = motor.control.limits()
    assert s == speed, "speed error on limits"
    assert acc == acceleration, "accel error on limits"
    assert act == actuation, "actuation error on limits"

    pid = motor.control.pid()
    if DETAILS:
        print(f"motor.control.pid() {pid}")

    # Test V2 PID syntax (six parameters).
    # V2   doc: pid(kp, ki, kd, integral_range, integral_rate, feed_forward)
    # V3.6 doc: pid(kp, ki, kd, integral_deadzone, integral_rate)
    try:
        kp, ki, kd, integral_range, integral_rate, feed_forward = (
            motor.control.pid()
        )
        motor.control.pid(
            kp, ki, kd, integral_range, integral_rate, feed_forward
        )
    except Exception as ex:
        err_count += 1
        print(f"\tPID V2 syntax failed: {ex}")

        # V4 alternative (five parameters).
        try:
            kp, ki, kd, integral_deadzone, integral_rate = (
                motor.control.pid()
            )
            motor.control.pid(
                kp, ki, kd, integral_deadzone, integral_rate
            )
            print(f"\tPID V4 alternative OK: {motor.control.pid()}"
            )
        except Exception as v4_ex:
            err_count += 1
            print(f"PID V4 alternative failed: {v4_ex}")


    #	Description: Gets or sets the PID values for position and speed control.
    tol1 = motor.control.target_tolerances()
    if DETAILS:
        print(f"motor.control.target_tolerances() {tol1}")
    s, p = motor.control.target_tolerances()
    motor.control.target_tolerances(s,p)
    # Description: Gets or sets the tolerances that say when a maneuver is done.
    tol2 = motor.control.target_tolerances()
    if DETAILS:
        print(f"motor.control.target_tolerances() {tol2}")

    # Description: Gets or sets stalling tolerances.
    tol3 = motor.control.stall_tolerances()
    if DETAILS:
        print(f"motor.control.stall_tolerances() {tol3}")
    s, t = motor.control.stall_tolerances()
    motor.control.stall_tolerances(s,t)
    speed, time = motor.control.stall_tolerances()
    if DETAILS:
        print(f"motor.control.stall_tolerances({s},{t}) {speed}, {time}")
        print(f"motor.control.stall_tolerances() {motor.control.stall_tolerances()}")

    assert s == speed, f"speed error on stall_tolerances {speed} should be {s}"
    assert t == time, f"time error on stall_tolerances {time} should be {t}"

    motor.stop()  # as the end of the motor section

try:  # see if the touch sensor is on Port S1
        # class TouchSensor(port)
            # Description: LEGO® MINDSTORMS® EV3 Touch Sensor.
        ts = TouchSensor(Port.S1)
        # Description: Checks if the sensor is pressed.
        pr = ts.pressed()
        if DETAILS:
            print(f"ts.pressed() {pr}")
except:
    print("\nNo touch sensor on Port.S1, try Gyro\n")
    # class GyroSensor(port,positive_direction=Direction.CLOCKWISE)
    # Description: LEGO® MINDSTORMS® EV3 Gyro Sensor.
    try:
        gs = GyroSensor(Port.S1)
        # Gets the speed (angular velocity) of the sensor.
        sp = gs.speed()
        if DETAILS:
            print(f"gs.speed() {sp}")
        # Gets the accumulated angle of the sensor.
        ang = gs.angle()
        if DETAILS:
            print(f"gs.angle() {ang}")
        # If you use the angle() method,
        # you cannot use the speed() method in the same program.
        # Doing so would reset the sensor angle to zero every time you read the speed.

        # Sets the rotation angle of the sensor to a desired value.
        ang2 = gs.reset_angle(angle)
        if DETAILS:
            print(f"gs.reset_angle(angle) {ang2}")

    except:
        err_count += 1
        print("\nNo gyro sensor on Port.S1\n")

try:
    # class ColorSensor(port)
    # Description: LEGO® MINDSTORMS® EV3 Color Sensor.
    step = 0
    cs = ColorSensor(Port.S2)
    step = 1
    # Description: Measures the color of a surface.
    clr = cs.color()
    if DETAILS:
        print(f"cs.color() {clr}")

    step = 2
    # Description: Measures the ambient light intensity.
    amb = cs.ambient()
    if DETAILS:
        print(f"cs.ambient() {amb}")

    step = 3
    # Description: Measures the reflection of a surface using a red light.
    refl = cs.reflection()
    if DETAILS:
        print(f"cs.reflection() {refl}")

    step = 4
    # Description: Measures the reflection of a surface
    # using a red, green, and then a blue light.
    rgb = cs.rgb()
    if DETAILS:
        print(f"cs.rgb() {rgb}")

except Exception as ex:
    err_count += 1
    if ex.args[0] in NODEV:
        err_count += 1
        print("\nNo color sensor on Port.S2")
    else:
        err_count += 1
        print(f"\t{ex} in step {step}\n")

try:
    # class InfraredSensor(port)
    # Description: LEGO® MINDSTORMS® EV3 Infrared Sensor and Beacon.
    ir = InfraredSensor(Port.S3)

    dist = ir.distance()
    if DETAILS:
        print(f"ir.distance() {dist}")

    channel = 1

    # Description: Measures the relative distance and angle between the remote and the
    # infrared sensor.
    bkn = ir.beacon(channel)
    if DETAILS:
        print(f"ir.beacon(channel) {bkn}")

    # Description: Checks which buttons on the infrared remote are pressed.
    but = ir.buttons(channel)
    if DETAILS:
        print(f"ir.buttons(channel) {but}")

    # Description: Checks which buttons on the infrared remote are pressed.
    kpad = ir.keypad()
    if DETAILS:
        print(f"ir.keypad() {kpad}")

except Exception as ex:
    err_count += 1
    if ex.args[0] in NODEV:
        print("\nNo infrared sensor on Port.S3\n")
    else:
        print(f"\t{ex}\n")

try:
    # class UltrasonicSensor(port)
    # Description: LEGO® MINDSTORMS® EV3 Ultrasonic Sensor.
    us = UltrasonicSensor(Port.S4)

    # Description: Measures the distance between the sensor and an object using
    # ultrasonic sound waves.
    usdist1 = us.distance(silent=False)
    if DETAILS:
        print(f"us.distance(silent=False) {usdist1}")

    # Description: Checks for the presence of other ultrasonic sensors
    # by detecting ultrasonic sounds.
    uspres = us.presence()
    if DETAILS:
        print(f"us.presence() {uspres}")

    # Description: Measures the distance between the sensor and an object using
    # ultrasonic sound waves.
    usdist2 = us.distance(silent=True)
    if DETAILS:
        print(f"us.distance(silent=True) {usdist2}")

except Exception as ex:
    err_count += 1
    if ex.args[0] in NODEV:
        print("\nNo ultrasonic sensor on Port.S4\n")
    else:
        print(f"\t{ex}\n")

print(f"\nDone with {err_count} error(s)")
