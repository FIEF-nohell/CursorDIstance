from asyncio.windows_events import NULL
from win32api import GetSystemMetrics
import pyautogui as pa
from math import sqrt
import time

#  Change these numbers to fit your screen
screenWidthInCentimeters = 31
screenHeightInCentimeters = 17.5

screenWidthInPixels = GetSystemMetrics(0)
screenHeightInPixels = GetSystemMetrics(1)
xtemp, ytemp = NULL, NULL
stack, counter = 0, 0
xPixelRatio = round(screenWidthInPixels/screenWidthInCentimeters, 1)
yPixelRatio = round(screenHeightInPixels/screenHeightInCentimeters, 1)
avrgRatio = round(((xPixelRatio + yPixelRatio) / 2), 1)

print("Screen Resolution: " + str(screenWidthInPixels) + " x " + str(screenHeightInPixels))
print("Screen Resolution in cm: " + str(screenWidthInCentimeters) + "cm x " + str(screenHeightInCentimeters) + "cm")
print("Screen px to cm Ratio: " + str(xPixelRatio) + " x " + str(yPixelRatio))
print("Screen Ratio Average: " + str(avrgRatio))

def PixelToMetric(pixels):
    return ((1/avrgRatio)*pixels)

def log():
    logFile = open("log.txt", "r")
    contentString = logFile.readline()
    content = float(contentString[0:contentString.find(" m")])
    logFile.close()
    logFile = open("log.txt", "w")
    logFile.write(str(round(content + stack, 2)) + " m")
    logFile.close()

while True:
    time.sleep(0.05)
    counter = counter + 1
    x, y= pa.position()
    if(x != xtemp and xtemp != NULL or y != ytemp and ytemp != NULL):
        xdelta = PixelToMetric(abs(x - xtemp))
        ydelta = PixelToMetric(abs(y - ytemp))        
        stack = float(stack + ((sqrt((xdelta * xdelta) + (ydelta * ydelta))))/100)
    xtemp = x
    ytemp = y
    if(counter >= 100):
        log()
        counter = 0            
        stack = 0