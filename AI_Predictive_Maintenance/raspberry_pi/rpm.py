import random
import time

try:
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    SENSOR = 23
    GPIO.setup(SENSOR, GPIO.IN)
    count = 0

    def pulse(channel):
        global count
        count += 1

    GPIO.add_event_detect(SENSOR, GPIO.FALLING, callback=pulse)
except Exception:
    GPIO = None
    count = 0

    def pulse(channel):
        global count
        count += 1


def get_rpm():
    global count
    if GPIO is not None:
        count = 0
        time.sleep(1)
        rpm = count * 60
        return int(rpm)
    return random.randint(50, 174)