# sytax check for tools doc from pybricks V2

from pybricks.hubs import EV3Brick    
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Color, Direction, Port


# Initialize the EV3
ev3 = EV3Brick()

port = Port.S1
mode = 1  # No idea whatit should be.
values = (0, 1, 2, 3, 4)  # Just a gamble value
address = address = 0xD2 >> 1  # shift 1 bit to get a LEGO type of address

# for x in dir(ev3):
#     if not x.startswith("__"):
#         print(f"\t{x}")
# print()

# class StopWatch
#         Description: A stopwatch to measure time intervals. Similar to the stopwatch feature on your phone.
try:
    dev = StopWatch()
    wait(500)
    print(f"1 Current time {dev.time():>5}")
    # Description: Gets the current time of the stopwatch.
    wait(500)
    dev.pause()
    wait(500)
    # Description: Pauses the stopwatch.
    print(f"2 Current time {dev.time():>5}")
    wait(500)
    dev.resume()
    wait(500)
    # Description: Resumes the stopwatch.
    print(f"3 Current time {dev.time():>5}")

    dev.reset()
    # Description: Resets the stopwatch time to 0.
    print(f"4 Current time {dev.time():>5}")
    wait(500)
    print(f"5 Current time {dev.time():>5}")
    wait(500)
except Exception as e:
    print(f"\tNot supported: {'StopWatch':<20} \t{e}\n")

print()
# class DataLog
# Description: Create a file and log data.
try:
    headers = ("col1", "col2")
    from pybricks.tools import DataLog
    dev = DataLog(*headers,name='log',timestamp=True,extension='csv',append=False)

    log(*values)
    # Description: Saves one or more values on a new line in the file.

    wait(500)
except Exception as e:
    print(f"\tNot supported: {'DataLog':<20} \t{e}\n")
