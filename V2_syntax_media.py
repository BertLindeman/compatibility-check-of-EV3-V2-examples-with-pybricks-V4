# ============================================================
# Pybricks EV3 Media / Parameter Syntax Checker
# Tests V2 (pybricks.media.ev3dev) → V4 (pybricks.parameters)
# import fallbacks for ImageFile, Image, SoundFile, Font
# ============================================================

from pybricks import version
print(f"Pybricks version: {version}\n")

from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.parameters import Color, Port

hub = EV3Brick()

# ── Helpers ──────────────────────────────────────────────────
def try_import(name, old_path, new_path):
    """Try old import first, fall back to new; return class or None."""
    try:
        mod = __import__(old_path, None, None, [name])   # positional, no kwargs
        cls = getattr(mod, name)
        print(f"  [{name}] loaded from {old_path}")
        return cls
    except Exception:
        pass
    try:
        mod = __import__(new_path, None, None, [name])   # positional, no kwargs
        cls = getattr(mod, name)
        print(f"  [{name}] loaded from {new_path}")
        return cls
    except Exception as e:
        print(f"  [{name}] NOT available: {e}")
        return None

OLD = "pybricks.media.ev3dev"
NEW = "pybricks.parameters"

# ── 01  ImageFile ─────────────────────────────────────────────
print("=== 01 ImageFile ===")
ImageFile = try_import("ImageFile", OLD, NEW)

if ImageFile is not None:
    try:
        names = [n for n in dir(ImageFile) if not n.startswith("_")]
        print(f"  Found {len(names)} ImageFile entries\n")
        for name in names:
            hub.screen.clear()
            image = getattr(ImageFile, name)
            print(f"  Showing ImageFile.{name}")
            hub.screen.print(name)
            x, y = (0, 0) if name == "PYBRICKS_JOIN" else (40, 50)

            try:
                hub.screen.draw_image(x, y, image)          # V4 positional
            except TypeError:
                hub.screen.draw_image(source=image, X=x, Y=y)  # V2 keyword fallback
            wait(2000)
        hub.screen.clear()
    except Exception as e:
        print(f"  [ImageFile display] failed: {e}")
else:
    print("  Skipping ImageFile display — class unavailable")

# ── 02  Image ─────────────────────────────────────────────────
print("\n=== 02 Image ===")
Image = try_import("Image", OLD, NEW)

if Image is not None and ImageFile is not None:
    try:
        source = getattr(ImageFile, "WRENCH17", None) or getattr(ImageFile, dir(ImageFile)[0])
        img = Image(source, sub=False)
        X1, Y1, X2, Y2 = 0, 0, img.width, img.height
        print(f"  Image size: {img.width} x {img.height}")

        try:
            img.draw_text(0, 0, str(source), text_color=Color.BLACK, background_color=None)
            print("  draw_text         OK")
        except Exception as e:
            print(f"  draw_text         FAIL: {e}")

        try:
            img.draw_pixel(0, 0, color=Color.BLACK)
            print("  draw_pixel        OK")
        except Exception as e:
            print(f"  draw_pixel        FAIL: {e}")

        try:
            img.draw_line(X1, Y1, X2, Y2, width=1, color=Color.BLACK)
            print("  draw_line         OK")
        except Exception as e:
            print(f"  draw_line         FAIL: {e}")

        try:
            img.draw_box(X1, Y1, X2, Y2, r=0, fill=False, color=Color.BLACK)
            print("  draw_box          OK")
        except Exception as e:
            print(f"  draw_box          FAIL: {e}")

        try:
            img.draw_circle(X1, Y1, r=12, fill=False, color=Color.BLACK)
            print("  draw_circle       OK")
        except Exception as e:
            print(f"  draw_circle       FAIL: {e}")

        try:
            img.draw_image(0, 0, source, transparent=None)
            print("  draw_image        OK")
        except Exception as e:
            print(f"  draw_image        FAIL: {e}")

        try:
            img.load_image(source)
            print("  load_image        OK")
        except Exception as e:
            print(f"  load_image        FAIL: {e}")

        try:
            img.clear()
            print("  clear             OK")
        except Exception as e:
            print(f"  clear             FAIL: {e}")

        try:
            img.save("test_output.png")
            print("  save              OK")
        except Exception as e:
            print(f"  save              FAIL: {e}")

    except Exception as e:
        print(f"  [Image init] failed: {e}")
else:
    print("  Skipping Image tests — class or ImageFile unavailable")

# ── 03  SoundFile ─────────────────────────────────────────────
print("\n=== 03 SoundFile ===")
SoundFile = try_import("SoundFile", OLD, NEW)

if SoundFile is not None:
    try:
        names = [n for n in dir(SoundFile) if not n.startswith("_")]
        print(f"  Found {len(names)} SoundFile entries:")
        for n in names:
            print(f"    SoundFile.{n}")
        wait(500)
    except Exception as e:
        print(f"  [SoundFile enumerate] failed: {e}")
else:
    print("  Skipping SoundFile — class unavailable")

# ── 04  Font (DEFAULT only) ───────────────────────────────────
print("\n=== 04 Font ===")
Font = try_import("Font", OLD, NEW)

if Font is not None:
    # List available class members
    try:
        members   = [n for n in dir(Font) if not n.startswith("__") and not n.startswith("text_")]
        txt_meths = [n for n in dir(Font) if not n.startswith("__") and     n.startswith("text_")]
        print("  Available constants:", ", ".join(members))
        print("  Text methods:      ", ", ".join(txt_meths))
    except Exception as e:
        print(f"  [Font.dir] failed: {e}")

    # Test Font.DEFAULT
    try:
        font = Font.DEFAULT
        print(f"\n  Font.DEFAULT      : {font}")

        try:
            print(f"  family            : {font.family}")
        except Exception as e:
            print(f"  family            FAIL: {e}")

        try:
            print(f"  style             : {font.style}")
        except Exception as e:
            print(f"  style             FAIL: {e}")

        try:
            print(f"  width             : {font.width}")
        except Exception as e:
            print(f"  width             FAIL: {e}")

        try:
            print(f"  height            : {font.height}")
        except Exception as e:
            print(f"  height             FAIL: {e}")

        sample = "Hello EV3"
        try:
            print(f"  text_width('{sample}') : {font.text_width(sample)}")
        except Exception as e:
            print(f"  text_width        FAIL: {e}")

        try:
            print(f"  text_height('{sample}'): {font.text_height(sample)}")
        except Exception as e:
            print(f"  text_height       FAIL: {e}")

        # Test set_font on a screen Image if available
        if Image is not None:
            try:
                screen_img = Image(hub.screen)
                screen_img.set_font(font)
                print("  set_font on screen OK")
            except Exception as e:
                print(f"  set_font          FAIL: {e}")

        wait(500)
    except Exception as e:
        print(f"  [Font.DEFAULT] failed: {e}")
else:
    print("  Skipping Font tests — class unavailable")

# ── Done ──────────────────────────────────────────────────────
print("\n=== Syntax check complete ===")

