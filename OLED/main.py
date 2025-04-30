from machine import Pin, SoftI2C
import ssd
from time import sleep

# ESP32 Pin assignment
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

"""
OLED -> ESP32
GND -> GND
VCC -> 3V3
SCL -> D22
SDA -> D21
"""
 
oled_width = 128
oled_height = 64
oled = ssd.SSD1306_I2C(oled_width, oled_height, i2c)
 
oled.text('Welcome', 0, 0)
oled.text('OLED Display', 0, 10)
oled.text('how2electronics', 0, 20)
oled.text('Makerfabs', 0, 30)
        
oled.show()

sleep(3)

oled.fill(0) # Clear the display

oled.text('New Display', 0, 0)
oled.text('Other Display', 0, 10)
oled.text('Blah blah blah', 0, 20)
oled.text('none', 0, 30)
        
oled.show()