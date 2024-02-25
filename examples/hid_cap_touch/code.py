import board
import time
import touchio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

while True:
    if touch1.value: # If touch pad 1 is touched ...
        while touch1.value: #wait for release
            time.sleep(0.1)
        keyboard.send(Keycode.SHIFT, Keycode.A) # then send keypress

    if touch2.value: #if touch pad 2 is touched ...
        while touch2.value: #wait for release
            time.sleep(0.1)
        keyboard_layout.write("Hello World!\n") #then send string.
