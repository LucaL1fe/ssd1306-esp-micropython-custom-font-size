# ssd1306-esp-micropython-custom-font-size

Hello, I was frustrated with the default font size of the OLED display SSD1306 while using MicroPython on an ESP32. After searching for a solution and finding none, I decided to create one myself by borrowing and modifying existing code.

Interested?

![image](https://github.com/LucaL1fe/ssd1306-esp-micropython-custom-font-size/assets/150456195/7d78d81b-2b13-4366-b096-b6454cd18671)

Here's what you need to do:

1. Copy and paste `ssd1306.py` and `example.py` into the same directory on the ESP32.
2. Execute `example.py` and it should work.

The key is the new `write_text()` function in `ssd1306.py`.

```python
oled.write_text(f"{i}%", 5, 15, 5)  # Text, Position x, Position y, **font size multiplier**
```

I hope this helps! If it does, a star would be wonderful :D

Credits:
- The base `ssd1306.py` is from: https://github.com/micropython/micropython-esp32/blob/esp32/drivers/display/ssd1306.py
- Big thanks to the original creator who implemented this upscale idea for the Pico: https://github.com/dhargopala/pico-custom-font/blob/main/lcd_lib.py
