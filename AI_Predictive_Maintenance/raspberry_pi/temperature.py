import random

try:
    from w1thermsensor import W1ThermSensor
    sensor = W1ThermSensor()
except Exception:
    sensor = None


def get_temperature():
    if sensor is not None:
        try:
            return round(sensor.get_temperature(), 2)
        except Exception:
            pass
    return round(random.uniform(25.0, 50.0), 2)