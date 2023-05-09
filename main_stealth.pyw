import math
import pyautogui
import time

PPI = 109  # Change this value to the PPI of your screen
previous_x, previous_y = pyautogui.position()
distance_traveled = 0

start_time = time.time()

with open("log.txt", "r+") as log_file:
    try:
        distance_traveled = float(log_file.read())
    except:
        distance_traveled = 0.0
    while True:
        current_x, current_y = pyautogui.position()
        distance = math.sqrt((current_x - previous_x) ** 2 + (current_y - previous_y) ** 2)
        distance_in_meters = (distance / PPI) * 0.0254
        distance_traveled += distance_in_meters
        previous_x, previous_y = current_x, current_y
        print("Distance traveled: {:.2f} m".format(distance_traveled), end="\r")
        if (time.time() - start_time) >= 1:
            log_file.seek(0)  # Move the cursor to the beginning of the file
            log_file.write("{:.2f}".format(distance_traveled))
            log_file.truncate()  # Truncate the remaining file content
            log_file.flush()  # Flush the buffer to write immediately
            start_time = time.time()
        time.sleep(0.01)
