
from pybricks import version 
from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.parameters import Color
hub = EV3Brick()

# define variables used in the doc
color = Color.GREEN  # EV3 only has RED GREEN and ORANGE
notes = ['C4/4', 'C4/4', 'G4/4', 'G4/4']

print(hub.buttons.pressed())
#	Description: Checks which buttons are currently pressed.
wait(250)

hub.light.on(color)
#	Description: Turns on the light at the specified color.
wait(250)

hub.light.off()
#	Description: Turns off the light.
wait(250)

# NOT SO LOUD please
hub.speaker.volume(5)

hub.speaker.beep(frequency=500,duration=100)
#	Description: Play a beep/tone.
wait(250)

hub.speaker.play_notes(notes,tempo=120)
#	Description: Plays a sequence of musical notes.
wait(250)

try:
    hub.speaker.play_file(file_name)
    #	Description: Plays a sound file.
    wait(250)
except:
    print(f"\tNot supported: hub.speaker.play_file ")

try:
    hub.speaker.say(text)
    #	Description: Says a given text string.
    wait(250)
except:
    print(f"\tNot supported: hub.speaker.say ")

try:
    hub.speaker.set_speech_options(language=None,voice=None,speed=None,pitch=None)
    #	Description: Configures speech settings used by thesay()method.
    wait(250)
except:
    print(f"\tNot supported: hub.speaker.set_speech_options ")

try:
    hub.speaker.set_volume(volume,which='_all_')
    #	Description: Sets the speaker volume.
    wait(250)
except:
    print(f"\tNot supported: hub.speaker.set_volume - use hub.speaker.volume(nn)")


hub.screen.clear()
#	Description: Clears the screen. All pixels on the screen will be set toColor.WHITE.
wait(250)

x = 10
y = 10
text = "Text"
hub.screen.draw_text(x,y,text,text_color=Color.BLACK,background_color=None)
#	Description: Draws text on the screen.
wait(1000)

hub.screen.print("\nPlop", text ,sep='\t',end='\n')
#	Description: Prints a line of text on the screen.
wait(1000)

try:
    # was: from pybricks.media.ev3dev import Font
    from pybricks.parameters import Font
    tiny_font = Font(size=6)
    big_font = Font(size=24, bold=True)
    chinese_font = Font(size=24, lang='zh-cn')
    hub.screen.set_font(font)
    #	Description: Sets the font used for writing on the screen.
    wait(250)
except:
    print(f"\tNot supported: hub.speaker.set_font")

try:
    from pybricks.media.ev3dev import Image, ImageFile
except ImportError:
    print("\tImportError: no module named 'pybricks.media.ev3dev' use parameters")
    from pybricks.parameters import Image, ImageFile

try:
    # It takes some time to load images from the SD card, so it is best to load
    # them once at the beginning of a program like this:
    from pybricks.media.ev3dev import Image, ImageFile
except ImportError:
    from pybricks.parameters import Image, ImageFile

try:
    source = Image(ImageFile.EV3_ICON)
    hub.screen.load_image(source)
except:
    print(f"\tNot supported: hub.screen.load_image")

try:
    hub.screen.draw_image(x,y,source,transparent=None)
    #	Description: Draws thesourceimage on the screen.
    wait(250)
except:
    print(f"\tNot supported: hub.screen.draw_image")

hub.screen.draw_pixel(x,y,color=Color.BLACK)
#	Description: Draws a single pixel on the screen.
wait(1000)

x1 = 45
y1 = 45
x2 = 95
y2 = 80
hub.screen.draw_line(x1,y1,x2,y2,width=1,color=Color.BLACK)
#	Description: Draws a line on the screen.
wait(1000)

x1 = 45
y1 = 45
x2 = 95
y2 = 80
hub.screen.draw_box(x1,y1,x2,y2,r=0,fill=False,color=Color.BLACK)
#	Description: Draws a box on the screen.
wait(1000)

x = 55
y = 55
r = 35
hub.screen.draw_circle(x,y,r,fill=True,color=Color.BLACK)
#	Description: Draws a circle on the screen.
wait(1000)

print("hub.screen.width", hub.screen.width)
#	Description: Gets the width of the screen in pixels.
wait(250)

print("hub.screen.height", hub.screen.height)
#	Description: Gets the height of the screen in pixels.
wait(250)

try:
    hub.screen.save(filename)
    #	Description: Saves the screen as a png file.
    wait(250)
except:
    print(f"\tNot supported: hub.screen.save")

print("hub.battery.voltage():", hub.battery.voltage(), "mV")
#	Description: Gets the voltage of the battery.
wait(250)

print("hub.battery.current():", hub.battery.current(), "mA")
#	Description: Gets the current supplied by the battery.
wait(250)

print("done on", version)
