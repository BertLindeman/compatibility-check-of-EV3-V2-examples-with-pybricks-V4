# syntax check for tools doc from pybricks V2

DETAILS = False  # print values to see if all is correct. For the error report set DETILS to False

dir_start = dir()
from pybricks.tools import *

if DETAILS:
    for __x in dir():
        if not __x.startswith("__"):
            if __x in dir_start:
                print(f"start \t{__x}")
            else:
                print(f"\t{__x}")
    print()

from pybricks import version
print(f"Pybricks version: {version}\n")

from pybricks.hubs import EV3Brick    
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Color, Direction, Port

# Initialize the EV3
ev3 = EV3Brick()

port = Port.S1
mode = 1  # No idea whatit should be.
values = (0, 1, 2, 3, 4)  # Just a gamble value
address = address = 0xD2 >> 1  # shift 1 bit to get a LEGO type of address

# class StopWatch
#         Description: A stopwatch to measure time intervals. 
#         Similar to the stopwatch feature on your phone.
try:
    dev = StopWatch()
    wait(500)

    # Description: Gets the current time of the stopwatch.
    val1 = dev.time()
    if DETAILS:
        print(f"1 Current time      {val1:>5}")
    wait(500)
    val2 = dev.time()
    # Description: Pauses the stopwatch.
    dev.pause()
    if DETAILS:
        print(f"2 time after pause  {val2:>5}")
    wait(500)

    val3 = dev.time()
    if DETAILS:
        print(f"3 time after pause  {val3:>5}")
    wait(500)

    # Description: Resumes the stopwatch.
    dev.resume()
    wait(500)
    val4 = dev.time()
    if DETAILS:
        print(f"4 time after resume {val4:>5}")

    # Description: Resets the stopwatch time to 0.
    dev.reset()
    val5 = dev.time()
    if DETAILS:
        print(f"5 time after reset  {val5:>5}")
        
    wait(500)
    val6 = dev.time()
    if DETAILS:
        print(f"6 time after wait   {val6:>5}")
    wait(500)
except Exception as e:
    print(f"\n\tNot supported: {'StopWatch':<20} \t{e}\n")

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
    print(f"\n\tNot supported: {'DataLog':<20} \t{e}\n")

# ── Done ──────────────────────────────────────────────────────
print("\n=== Syntax check complete ===")
