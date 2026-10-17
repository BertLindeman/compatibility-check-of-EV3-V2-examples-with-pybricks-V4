# syntax check for robnxtdevices part 2 doc from pybricks V2

from pybricks import version
print(f"Pybricks version: {version}\n")
from uerrno import ENODEV, ETIMEDOUT

# from pybricks.hubs import EV3Brick
from pybricks.tools import wait, multitask, run_task
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.nxtdevices import SoundSensor, TemperatureSensor, EnergyMeter, VernierAdapter
# hub = EV3Brick()

# Needed sensors for this test:
# Port.S1 - NXT sound sensor
# Port.S2 - NXT temperature sensor  (not available here)
# Port.S3 - NXT energy sensor       (not available here)
# Port.S4 - NXT Vernier sensor      (not available here)

# define variables used in the doc
color = Color.GREEN  # EV3 only has RED, GREEN and ORANGE

DETAILS = False  # print values to see if all is correct. For the error report set DETILS to False

try:
	# Description: LEGO® MINDSTORMS® NXT Sound Sensor.
    ss = SoundSensor(Port.S1)

	# intensity: Measures the ambient sound intensity (loudness).
    try:
        for i in range(3):
            val1 = ss.intensity(audible_only=False)
            if DETAILS:
                print(f"ss.intensity(audible_only=False) {val1}")
                wait(500)
        for i in range(3):
            val1 = ss.intensity(audible_only=True)
            if DETAILS:
                print(f"ss.intensity(audible_only=True)  {val1}")
                wait(500)
    except Exception as ex:
        print(f"\tException on SoundSensor         \t{ex}\n")
except OSError as ex:
    if ex.args[0] != ENODEV:
        print(f"\tNo SoundSensor available or different device on Port.S1 \t{ex}\n")
    else:
        print(f"\tNo SoundSensor attached on Port.S1\n")
except Exception  as ex:
    print(f"\tNot supported: SoundSensor         \t{ex}\n")

try:
    ts = TemperatureSensor(Port.S2)
	# Description: LEGO® MINDSTORMS® NXT Temperature Sensor.
    try:
        # Description: Measures the temperature.
        for i in range(5):
            val1 = ts.temperature()
            if DETAILS:
                print(f"ts.temperature() {val1}")
                wait(500)
    except Exception as ex:
        print(f"\tException on TemperatureSensor         \t{ex}\n")
except OSError as ex:
    if ex.args[0] != ENODEV:
        print(f"\tNo TemperatureSensor available or different device on Port.S2 \t{ex}\n")
    else:
        print(f"\tNo TemperatureSensor attached on Port.S2\n")

except Exception  as ex:
    print(f"\tNot supported: TemperatureSensor \t{ex}\n")

try:
    em = EnergyMeter(Port.S3)
	# Description: LEGO® MINDSTORMS® Education NXT Energy Meter.
    if DETAILS:
        print(end="\tdir of EnergyMeter:")
        for __x in sorted(dir(em)):
            if not __x.startswith("__"):
                print(end="\t" + __x)
        print("\n")
    try:
        for i in range(5):
            # Description: Gets the total available energy stored in the battery.
            val1 = em.storage()
            if DETAILS:
                print(f"em.storage() {val1}")
                wait(500)
        for i in range(5):
            # Description: Measures the electrical signals at the input (bottom) side
            # of the energy meter.
            val1 = em.input()
            if DETAILS:
                print(f"em.input() {val1}")
                wait(500)
        for i in range(5):
            # Description: Measures the electrical signals at the output (top) side
            # of the energy meter.
            val1 = em.output()
            if DETAILS:
                print(f"em.output() {val1}")
                wait(500)
    except Exception as ex:
        print(f"\tException on EnergyMeter on Port.S3\t{ex}\n")
except OSError as ex:
    if ex.args[0] != ENODEV:
        print(f"\tNo EnergyMeter available or different device on Port.S3 \t{ex}\n")
    else:
        print(f"\tNo EnergyMeter attached on Port.S3\n")
except Exception  as ex:
    print(f"\tNot supported: EnergyMeter         \t{ex}\n")

def  return_raw_temp(voltage):
    return voltage

# class VernierAdapter(port,conversion=None)
# 	# Description: LEGO® MINDSTORMS® Education NXT/EV3 Adapter for Vernier Sensors.
try:
    va = VernierAdapter(Port.S4,  return_raw_temp)
    try:
        val = va.voltage()
        # voltage()
        # 	# Description: Measures the raw analog sensor voltage.

        val = va.conversion(3.3)
        # conversion(voltage)
        # 	# Description: Converts the raw voltage (mV) to a sensor value.

        val = va.value()
        # value()
        # 	# Description: Measures the sensorvoltage()and then
        #     # applies yourconversion()to give you the sensor value.
    except Exception as ex:
        print(f"\tNot supported: VernierAdapter         \t{ex}\n")

except OSError as ex:
    if ex.args[0] != ENODEV:
        print(f"\tNo VernierAdapter available or different device on Port.S4 \t{ex}\n")
    else:
        print(f"\tNo VernierAdapter attached on Port.S4\n")
except Exception  as ex:
    print(f"\tNot supported: VernierAdapter         \t{ex}\n")

# ── Done ──────────────────────────────────────────────────────
print("\n=== Syntax check complete ===")
