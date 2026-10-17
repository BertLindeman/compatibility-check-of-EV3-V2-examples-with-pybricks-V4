# syntax check for tools doc from pybricks V2

DETAILS = False  # print values to see if all is correct. For the error report set DETILS to False

from pybricks import version
print(f"Pybricks version: {version}\n")

from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.parameters import Color
hub = EV3Brick()

# define variables used in the doc
color = Color.GREEN  # EV3 only has RED GREEN and ORANGE
notes = ['C4/4', 'C4/4', 'G4/4', 'G4/4']

#	Description: Checks which buttons are currently pressed.
val1 = hub.buttons.pressed()
if DETAILS:
    print("Buttons pressed", val1)
wait(250)

#	Description: Turns on the light at the specified color.
hub.light.on(color)
wait(250)

#	Description: Turns off the light.
hub.light.off()
wait(250)

# NOT SO LOUD please
hub.speaker.volume(5)

#	Description: Play a beep/tone.
hub.speaker.beep(frequency=500,duration=100)
wait(250)

#	Description: Plays a sequence of musical notes.
hub.speaker.play_notes(notes,tempo=120)
wait(250)

try:
    #	Description: Plays a sound file.
    hub.speaker.play_file(file_name)
    wait(250)
except:
    print(f"\tNot supported: hub.speaker.play_file ")

try:
    #	Description: Says a given text string.
    hub.speaker.say(text)
    wait(250)
except:
    print(f"\tNot supported: hub.speaker.say ")

try:
    #	Description: Configures speech settings used by thesay()method.
    hub.speaker.set_speech_options(language=None,voice=None,speed=None,pitch=None)
    wait(250)
except:
    print(f"\tNot supported: hub.speaker.set_speech_options ")

try:
    #	Description: Sets the speaker volume.
    hub.speaker.set_volume(volume,which='_all_')
    wait(250)
except:
    print(f"\tNot supported: hub.speaker.set_volume - use hub.speaker.volume(nn)")


#	Description: Clears the screen. All pixels on the screen will be set toColor.WHITE.
hub.screen.clear()
wait(250)

x = 10
y = 10
text = "Text"
#	Description: Draws text on the screen.
hub.screen.draw_text(x,y,text,text_color=Color.BLACK,background_color=None)
wait(1000)

#	Description: Prints a line of text on the screen.
hub.screen.print("\nPlop", text ,sep='\t',end='\n')
wait(1000)

try:
    from pybricks.media.ev3dev import Font
except:
    print("\tImportError: no module 'pybricks.media.ev3dev' use 'pybricks.parameters'")
    from pybricks.parameters import Font

try:
    tiny_font = Font(size=6)
except Exception as ex:
    print(f"\tNot supported: Font(size=6): {ex}")

try:
    big_font = Font(size=24, bold=True)
except Exception as ex:
    print(f"\tNot supported: Font(size=24, bold=True): {ex}")

try:
    chinese_font = Font(size=24, lang='zh-cn')
except Exception as ex:
    print(f"\tNot supported: Font(size=24, lang='zh-cn'): {ex}")

try:
    hub.screen.set_font(Font.TERMINUS_16)
    hub.screen.print("Font.TERMINUS_16")
    wait(500)
except Exception as ex:
    print(f"\tNot supported: hub.screen.set_font: {ex}")
wait(250)

try:
    from pybricks.media.ev3dev import Image, ImageFile
except ImportError:
    from pybricks.parameters import Image, ImageFile

try:
    # It takes some time to load images from the SD card, so it is best to load
    # them once at the beginning of a program like this:
    from pybricks.media.ev3dev import Image, ImageFile
except ImportError:
    from pybricks.parameters import Image, ImageFile

try:
    source = Image(ImageFile._WRENCH17)
    try:
        hub.screen.load_image(source)
    except:
        print(f"\tNot supported: hub.screen.load_image")
except:
    print(f"\tNot supported: `source = Image(ImageFile._WRENCH17)`")
    print(f"\tNot TESTED:     hub.screen.load_image")

try:
    #	Description: Draws thesourceimage on the screen.
    hub.screen.draw_image(x,y,source,transparent=None)
    wait(250)
except:
    print(f"\tNot supported: hub.screen.draw_image")

#	Description: Draws a single pixel on the screen.
hub.screen.draw_pixel(x,y,color=Color.BLACK)
wait(1000)

x1 = 45
y1 = 45
x2 = 95
y2 = 80
#	Description: Draws a line on the screen.
hub.screen.draw_line(x1,y1,x2,y2,width=1,color=Color.BLACK)
wait(1000)

x1 = 45
y1 = 45
x2 = 95
y2 = 80
#	Description: Draws a box on the screen.
hub.screen.draw_box(x1,y1,x2,y2,r=0,fill=False,color=Color.BLACK)
wait(1000)

x = 55
y = 55
r = 35
#	Description: Draws a circle on the screen.
hub.screen.draw_circle(x,y,r,fill=True,color=Color.BLACK)
wait(1000)

#	Description: Gets the width of the screen in pixels.
hub.screen.print("hub.screen.width", hub.screen.width)
wait(250)

#	Description: Gets the height of the screen in pixels.
hub.screen.print("hub.screen.height", hub.screen.height)
wait(250)

try:
    #	Description: Saves the screen as a png file.
    hub.screen.save(filename)
    wait(250)
except:
    print(f"\tNot supported: hub.screen.save")

#	Description: Gets the voltage of the battery.
hub.screen.print("hub.battery.voltage():", hub.battery.voltage(), "mV")
wait(250)

#	Description: Gets the current supplied by the battery.
hub.screen.print("hub.battery.current():", hub.battery.current(), "mA")
wait(250)

# ── Done ──────────────────────────────────────────────────────
print("\n=== Syntax check complete ===")
