try:
    from RPLCD.i2c import CharLCD
    lcd = CharLCD('PCF8574', 0x27)
except Exception:
    lcd = None


def display(temp, vib, current, rpm, status):
    if lcd is None:
        return

    lcd.clear()
    lcd.write_string(f"T:{temp}C")

    lcd.cursor_pos = (1, 0)
    lcd.write_string(f"V:{vib}g")

    lcd.cursor_pos = (2, 0)
    lcd.write_string(f"I:{current}A")

    lcd.cursor_pos = (3, 0)
    lcd.write_string(f"{rpm}RPM {status}")