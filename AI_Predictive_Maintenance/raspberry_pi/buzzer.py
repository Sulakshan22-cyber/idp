try:
    import RPi.GPIO as GPIO
except Exception:
    GPIO = None

BUZZER = 18

if GPIO is not None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUZZER, GPIO.OUT)


def off():
    if GPIO is not None:
        GPIO.output(BUZZER, 0)


def on():
    if GPIO is not None:
        GPIO.output(BUZZER, 1)