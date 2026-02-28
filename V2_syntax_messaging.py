# syntax check for messaging doc from pybricks V2

from pybricks.hubs import EV3Brick    
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Color, Direction, Port


# for x in dir():
#     if not x.startswith("__"):
#         print(f"\t{x}")
# print()

# Initialize the EV3
ev3 = EV3Brick()

port = Port.S1
mode = 1  # No idea what it should be.
values = (0, 1, 2, 3, 4)  # Just a gamble value
address = address = 0xD2 >> 1  # shift 1 bit to get a LEGO type of address
name = "The other"
connection = None  # No idea yet what this should be

# class BluetoothMailboxServer 
# Description: Object that represents a Bluetooth connection from one or more remote EV3s.
try:
    from pybricks.messaging import BluetoothMailboxServer
    dev = BluetoothMailboxServer

    dev.wait_for_connection(count=1) 
	# Description: Waits for aBluetoothMailboxClienton a remote device to connect.

    dev.close() 
	# Description: Closes all connections.

    wait(500)
except Exception as e:
    print(f"\tNot supported: {'BluetoothMailboxServer':<22} {e}\n")


# class BluetoothMailboxClient
# Description: Object that represents a Bluetooth connection to one or more remote EV3s.
try:
    from pybricks.messaging import BluetoothMailboxClient
    dev = BluetoothMailboxClient()
    dev.connect(brick) 
	# Description: Connects to an BluetoothMailboxServer on another device.

    wait(500)
except Exception as e:
    print(f"\tNot supported: {'BluetoothMailboxClient':<22} {e}\n")

# class Mailbox(name,connection,encode=None,decode=None) 
# Description: Object that represents a mailbox containing data.
try:
    from pybricks.messaging import Mailbox
    dev = Mailbox(name,connection,encode=None,decode=None)
    dev.read() 
	# Description: Gets the current value of the mailbox.

    dev.send(value,brick=None) 
	# Description: Sends a value to this mailbox on connected devices.

    dev.wait() 
	# Description: Waits for the mailbox to be updated by remote device.

    dev.wait_new() 
	# Description: Waits for a new value to be delivered to the mailbox
    # that is not equal to the current value in the mailbox.

    wait(500)
except Exception as e:
    print(f"\tNot supported: {'BluetoothMailboxServer':<22} {e}\n")


# class LogicMailbox(name,connection) 
# Description: Object that represents a mailbox containing boolean data.
try:
    from pybricks.messaging import LogicMailbox
    dev = LogicMailbox(name, connection)
    wait(500)
except Exception as e:
    print(f"\tNot supported: {'LogicMailbox':<22} {e}\n")

# class NumericMailbox(name,connection) 
# Description: Object that represents a mailbox containing numeric data.
try:
    from pybricks.messaging import NumericMailbox
    dev = NumericMailbox(name,connection)
    wait(500)
except Exception as e:
    print(f"\tNot supported: {'NumericMailbox':<22} {e}\n")

# class TextMailbox(name,connection) 
# Description: Object that represents a mailbox containing text data.
try:
    from pybricks.messaging import TextMailbox
    dev = TextMailbox(name, connection)
    wait(500)
except Exception as e:
    print(f"\tNot supported: {'TextMailbox':<22} {e}\n")

