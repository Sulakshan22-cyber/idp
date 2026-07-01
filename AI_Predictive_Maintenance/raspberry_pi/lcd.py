try:
    from RPLCD.i2c import CharLCD
    lcd = CharLCD('PCF8574', 0x27)
except Exception:
    lcd = None


def display(temp, rpm, status):
    if lcd is None:
        return

    lcd.clear()
    lcd.write_string(f"T:{temp}C R:{rpm}")

    lcd.cursor_pos = (1, 0)
    lcd.write_string(f"Status: {status}")