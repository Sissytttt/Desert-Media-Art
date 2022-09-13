# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
import time
import board
import random

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.1

r = 0;
g = 0;
b = 0;

# the sky is becoming brighter
while r<150 and g<150 and b<150:
    led[0] = (r, g, b)
    r+=1
    g+=1
    b+=1
    time.sleep(0.05)
    
# the sun is rising
print("red")
led.brightness = 0.2
while r<255 and g>54 and b>20:
    led[0] = (r, g, b)
    r+=1
    g-=1
    b-=1
    time.sleep(0.05)
print(r, g, b)

# golden glow of the sun
print("yellow")
while g<166:
    led[0] = (r, g, b)
    g+=1
    #time.sleep(0.03)
print(r, g, b)


print("blue")
led.brightness = 0.2
while r > 20 and b < 220:
    led[0] = (r, g, b)
    r -= 1
    b += 1
    time.sleep(0.03)
print(r, g, b)

'''
print("white")
while r <255 and g < 255 and b < 255:
    r+=3
    g+=1
    b+=1
    time.sleep(0.03)
print(r, g, b)


print("blue")
while r > 20 and g > 180 and b > 230:
    led[0] = (r, g, b)
    r -= 12
    g -= 9
    b -= 1
    time.sleep(0.03)
print(r, g, b)

'''

# the sky is turing dark (cloudy)
print("dark")
while g > 100 and b > 120:
    led[0] = (r, g, b)
    g -= 1
    b -= 1
    time.sleep(0.03)
print(r, g, b)

while r>40:
    led[0] = (r, g, b)
    r -= 1
    g -= 1
    b -= 2
    time.sleep(0.1)
print(r, g, b)

# the storm begins
# ligntning
# use random function to create random flash
print("flash")
while r>0:
    led[0] = (r, g, b)
    r -= 1
    g -= 1
    b -= 2
    x = random.random()
    # strong flash with a light flash follows
    if x<0.1:
        led.brightness = 0.4
        led[0] = (255,255,255)
        time.sleep(0.1)
        led[0] = (0, 0, 0)
        time.sleep(0.1)
        led.brigtness = 0.1
        led[0] = (255,255,255)
        time.sleep(0.1)
    # medium long flash
    elif x<0.2:
        led.brightness = 0.3
        led[0] = (255,255,255)
        time.sleep(0.3);
    # weak short flash
    elif x<0.3:
        led.brightness = 0.2
        led[0] = (255,255,255)
        time.sleep(0.2);
    else:
        time.sleep(0.3)
print(r, g, b)


print("police")
# the polic light for 7 seconds
# the frequncy gets higher and higher, because I think the high frequncy can create a sense of tension
startT = time.monotonic()
sleeptime = 0.6
while (time.monotonic() - startT) < 7:
    led[0] = (255,0,0)
    time.sleep(sleeptime)
    led[0] = (0,0,255)
    time.sleep(sleeptime)
    sleeptime -= 0.05
