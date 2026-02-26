# sytax check for iodevices doc from pybricks V2

from uerrno import ENODEV
from pybricks.hubs import EV3Brick    
from pybricks.tools import wait
from pybricks.parameters import Color, Direction, Port
from pybricks.iodevices import LUMPDevice, AnalogSensor, I2CDevice, UARTDevice, DCMotor

# Initialize the EV3
ev3 = EV3Brick()

port = Port.S4
mode = 1  # No idea whatit should be.
values = (0, 1, 2, 3, 4)  # Just a gable value
address = address = 0xD2 >> 1  # shift 1 bit to get a LEGO type of address
data = "just a string"

# class LUMPDevice
try:
    dev = LUMPDevice(port)
        # Description: Devices using the LEGO UART Messaging Protocol.

except Exception as e:
    print(f"\tNot supported: {'LUMPDevice':<20} \t{e}\n")

try:
    dev.read(mode) 
        # Description: Reads values at a given mode.

    dev.write(mode,values) 
        # Description: Writes values to the sensor. Only selected sensors and modes support this.
    wait(500)
except Exception as e:
    print(f"\tNot supported: {'LUMPDevice':<20} read/write \t{e}\n")


# class AnalogSensor(port) 
# Description: Generic or custom analog sensor.
try:
    dev = AnalogSensor(port)
    try:
        print(f"dev.voltage() {dev.voltage()}") 
        # Description: Measures analog voltage.

        print(f"dev.resistance() {dev.resistance()}") 
        # Description: Measures resistance.

        print(f"dev.active() {dev.active()}") 
        # Description: Sets sensor to active mode. This sets pin 5 of the sensor port tohigh.

        print(f"dev.passive() {dev.passive()}") 
        # Description: Sets sensor to passive mode. This sets pin 5 of the sensor port tolow.
        wait(500)
    except Exception as e:
        print(f"\tNot supported: {'AnalogSensor':<20} functions\t{e}\n")

except OSError as ex:
    if ex.args[0] == ENODEV:
        # No device found on this port.
        print(f"\tNo AnalogSensor on {port}")
    else:
        print(f"\tNot supported: {'AnalogSensor':<20} \t{e}\n")



# class I2CDevice(port,address) 
# Description: Generic or custom I2C device.
reg = 0  # just took one
try:
    i2cdev = I2CDevice(port,address)
    try:
        i2cdev.read(reg,length=1) 
        # Description: Reads bytes, starting at a given register.

        i2cdev.write(reg,data=None) 
        # Description: Writes bytes, starting at a given register.

        wait(500)
    except Exception as e:
        print(f"\tNot supported: {'I2CDevice':<20} functions \t{e}\n")
except OSError as ex:
    if ex.args[0] == ENODEV:
        # No device found on this port.
        print(f"\tNo I2CDevice on {port}")
    else:
        print(f"\tNot supported: {'I2CDevice':<20} \t{e}\n")

except Exception as e:
    print(f"\tNot supported: {'I2CDevice':<20} \t{e}\n")
    

# class UARTDevice(port,baudrate,timeout=None) 
# Description: Generic UART device.
baudrate = 2400
try:
    UARTdev = UARTDevice(port,baudrate,timeout=None)
	# Description: Generic UART device.

    UARTdev.read(length=1) 
	# Description: Reads a given number of bytes from the buffer.

    UARTdev.read_all() 
	# Description: Reads all bytes from the buffer.

    UARTdev.write(data) 
	# Description: Writes bytes.

    UARTdev.waiting() 
	# Description: Gets how many bytes are still waiting to be read.

    UARTdev.clear() 
	# Description: Empties the buffer.

    wait(500)
except Exception as e:
    print(f"\tNot supported: {'UARTDevice':<20} \t{e}\n")

except OSError as ex:
    if ex.args[0] == ENODEV:
        # No device found on this port.
        print(f"\tNo UARTDevice on {port}")
    else:
        print(f"\tNot supported: {'UARTDevice':<20} \t{e}\n")

except Exception as e:
    print(f"\tNot supported: {'UARTDevice':<20} \t{e}\n")


# class DCMotor
duty = 25  # 25% duty cycle
try:
    DCdev = DCMotor(port,positive_direction=Direction.CLOCKWISE) 
    # Description: Generic class to control simple motors without rotation sensors, such as train motors.
    try:
        DCdev.dc(duty) 
        # Description: Rotates the motor at a given duty cycle (also known as “power”).

        DCdev.stop() 
        # Description: Stops the motor and lets it spin freely.

        wait(500)
    except Exception as e:
        print(f"\tNot supported: {'DCMotor':<20} functions\t{e}\n")

except OSError as ex:
    if ex.args[0] == ENODEV:
        # No device found on this port.
        print(f"\tNo DCdev on {port}")
    else:
        print(f"\tNot supported: {'DCdev':<20} \t{e}\n")

except Exception as e:
    print(f"\tNot supported: {'DCdev':<20} \t{e}\n")


# class Ev3devSensor 
# Description: Read values of an ev3dev-compatible sensor.
try:
    from pybricks.iodevices import Ev3devSensor
    try:
        dev = Ev3devSensor(port) 
        # Description: Read values of an ev3dev-compatible sensor.

        dev.sensor_index 
        # Description: Index of the ev3dev sysfslego-sensorclass.

        dev.port_index 
        # Description: Index of the ev3dev sysfslego-portclass.

        wait(500)
    except Exception as e:
        print(f"\tNot supported: {'Ev3devSensor':<20} functions \t{e}\n")
except ImportError:
    print("\tNot supported import: Ev3devDensor")


