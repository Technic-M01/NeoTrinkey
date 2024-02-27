import board
import time
import touchio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

import rd_network

import neopixel

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0, 0, 0)

num_pixels = 4

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=False)

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

num_cycles = 1

def setBrightness(index, newVal):
    px = pixels[index] # get tuple of rgb vals from current pixel
    rgb = list(px) #tuple of color vals as list

    for i in range(3):
        t = px[i]

        percentage = (newVal / 255) * 100 # get percentage of max brightness from the newVal
        pOfCurrent = (percentage / 100) * t # get percentage of current brightness from above

        p = (newVal / 255) * rgb[i]

        #print(i)
        #print(percentage)
        #print(pOfCurrent)

        rgb[i] = p

    pixels[index] = tuple(rgb)
    pixels.show()

def color_chase(color, wait):
    cycles = 0

    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)

    initialBrightness = 10
    while initialBrightness < 255:
        print(initialBrightness)

        for i in range(num_pixels):
            setBrightness(i, initialBrightness)
            print("set brightness for")
            print(i)
            time.sleep(0.1)

        initialBrightness += 5

#    while cycles < num_cycles:
#        for i in range(num_pixels):
#            v = pixels[i]
#            print(v)
#            setBrightness(i, 80)
#
#            time.sleep(1)
#
#        cycles += 1

print("init")

while True:
    if touch1.value: # If touch pad 1 is touched ...
        while touch1.value: #wait for release
            time.sleep(0.1)
        rd_network.bypassUAC()
        time.sleep(1)
        rd_network.pullASneaky()
        #hide()

    if touch2.value: #if touch pad 2 is touched ...
        while touch2.value: #wait for release
            time.sleep(0.1)
        #keyboard_layout.write("Hello World!\n") #then send string.
        #color_chase(CYAN, 0.1)
        color_chase(RED, 0.2)
        #color_chase(BLUE, 0.3)
        #color_chase(YELLOW, 0.4)
        #color_chase(GREEN, 0.5)
