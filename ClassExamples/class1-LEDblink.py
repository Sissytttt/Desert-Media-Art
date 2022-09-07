# blink  input/output - LED
# time.monotonic (time control)
# use code from dafruit
# https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/creating-and-editing-code

print("blink")

import board
import digitalio  # library in Python
import time

print("the basic LED is attached to pin " + str(board.LED))
print("It is now " + str(time.monotonic()))

# this variable gives access to the hardware pin
led = digitalio.DigitalInOut(board.LED)

# set the LED pin as an output so we can turn it on/off
led.direction = digitalio.Direction.OUTPUT

# record the starting time
startTime = time.monotonic()

# how long for blink (seconds)
secondsToBlink = 5

while (time.monotonic() - startTime) < secondsToBlink:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
    print("  time - %0.1f" % time.monotonic())
