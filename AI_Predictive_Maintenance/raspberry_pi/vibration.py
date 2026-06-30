import random

try:
    import board
    import busio
    import adafruit_adxl34x

    i2c = busio.I2C(board.SCL, board.SDA)
    accelerometer = adafruit_adxl34x.ADXL345(i2c)
except Exception:
    accelerometer = None


def get_vibration():
    if accelerometer is not None:
        try:
            x, y, z = accelerometer.acceleration
            magnitude = ((x**2 + y**2 + z**2) ** 0.5) / 9.81
            return round(magnitude, 2)
        except Exception:
            pass
    return round(random.uniform(0.5, 3.5), 2)