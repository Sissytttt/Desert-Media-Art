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


'''
----in interaction mode of python-----
>>>import digitalio
>>> import board
>>> led = digitalio.DigitalInOut(board.LED)
>>> dir(led)
['__class__', '__enter__', '__exit__', 'value', 'deinit', 'direction', 'pull', 'switch_to_input', 'switch_to_output']
>>> help(led.direction)
object digitalio.Direction.INPUT is of type Direction
  INPUT -- digitalio.Direction.INPUT
  OUTPUT -- digitalio.Direction.OUTPUT
>>>help(led.*anything*)
'''
