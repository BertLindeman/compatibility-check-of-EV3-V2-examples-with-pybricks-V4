from pybricks.hubs import EV3Brick
from pybricks.tools import wait, multitask, run_task
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.nxtdevices import SoundSensor, TemperatureSensor, EnergyMeter
# from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
hub = EV3Brick()

# Needed sensors for this test:
# Port.S1 - NXT sound sensor
# Port.S2 - NXT temperature sensor
# Port.S3 - NXT energy sensor

# define variables used in the doc
color = Color.GREEN  # EV3 only has RED GREEN and ORANGE

try:
    ss = SoundSensor(Port.S1)
	# Description: LEGO® MINDSTORMS® NXT Sound Sensor.
	# intensity: Measures the ambient sound intensity (loudness).
    wait(500)
	# Description: Checks if the sensor is pressed.
    for i in range(3):
        print(f"ss.intensity(audible_only=False) {ss.intensity(audible_only=False)}")
        wait(500)
    for i in range(3):
        print(f"ss.intensity(audible_only=True)  {ss.intensity(audible_only=True)}")
        wait(500)
except Exception as e:
    print(f"\tNot supported: SoundSensor         \t{e}\n")


try:
    ts = TemperatureSensor(Port.S2)
	# Description: LEGO® MINDSTORMS® NXT Temperature Sensor.
    wait(500)
	# Description: Measures the temperature.
    for i in range(5):
        print(f"ts.temperature() {ts.temperature()}")
        wait(500)
except Exception as e:
    print(f"\tNot supported: TemperatureSensor \t{e}\n")

try:
    em = EnergyMeter(Port.S3)
	# Description: LEGO® MINDSTORMS® Education NXT Energy Meter.

    for i in range(5):
        print(f"em.storage() {em.storage()}")
    	# Description: Gets the total available energy stored in the battery.
        wait(500)
    for i in range(5):
        print(f"em.input() {em.input()}")
        # Description: Measures the electrical signals at the input (bottom) side
        # of the energy meter.
        wait(500)
    for i in range(5):
        print(f"em.output() {em.output()}")
        # Description: Measures the electrical signals at the output (top) side
        # of the energy meter.
        wait(500)

except Exception as e:
    print(f"\tNot supported: EnergyMeter         \t{e}\n")


# class VernierAdapter(port,conversion=None)
# 	# Description: LEGO® MINDSTORMS® Education NXT/EV3 Adapter for Vernier Sensors.

# voltage()
# 	# Description: Measures the raw analog sensor voltage.

# conversion(voltage)
# 	# Description: Converts the raw voltage (mV) to a sensor value.

# value()
# 	# Description: Measures the sensorvoltage()and then
#     # applies yourconversion()to give you the sensor value.
