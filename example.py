from machine import Pin, SoftI2C
import ssd1306
import time

i2c = SoftI2C(sda=Pin(21), scl=Pin(22))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    for i in range(100):
       oled.write_text(f"{i}%", 5, 15, 5) #scale font with factor 5
       oled.show()       
       time.sleep(0.5)
