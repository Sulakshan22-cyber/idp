import random

try:
    import board
    import busio
    from adafruit_ads1x15.ads1115 import ADS1115
    from adafruit_ads1x15.analog_in import AnalogIn

    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS1115(i2c)
    chan = AnalogIn(ads, ADS1115.P0)
except Exception:
    chan = None


def get_current():
    if chan is not None:
        try:
            voltage = chan.voltage
            current = abs((voltage - 2.5) / 0.185)
            return round(current, 2)
        except Exception:
            pass
    return round(random.uniform(0.8, 3.8), 2)