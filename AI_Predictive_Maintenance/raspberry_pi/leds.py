try:
    import RPi.GPIO as GPIO
except Exception:
    GPIO = None

GREEN = 17
YELLOW = 27
RED = 22

if GPIO is not None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GREEN, GPIO.OUT)
    GPIO.setup(YELLOW, GPIO.OUT)
    GPIO.setup(RED, GPIO.OUT)


def healthy():
    if GPIO is not None:
        GPIO.output(GREEN, 1)
        GPIO.output(YELLOW, 0)
        GPIO.output(RED, 0)


def warning():
    if GPIO is not None:
        GPIO.output(GREEN, 0)
        GPIO.output(YELLOW, 1)
        GPIO.output(RED, 0)


def fault():
    if GPIO is not None:
        GPIO.output(GREEN, 0)
        GPIO.output(YELLOW, 0)
        GPIO.output(RED, 1)