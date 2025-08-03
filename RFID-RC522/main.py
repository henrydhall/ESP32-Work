"""
Uses code and instruction from here:
https://microcontrollerslab.com/raspberry-pi-pico-rfid-rc522-micropython/
Works great with my esp32-wroom-32

RC522   ->  ESP32
SDA     ->  D18
SCK     ->  D19
MOSI    ->  D21
MISO    ->  D22
GND     ->  GND
RST     ->  D23
3.3V    ->  3V3
"""
from machine import Pin, SPI

from time import sleep

from mfrc522 import MFRC522
import utime

reader = MFRC522(spi_id=0,sck=19,miso=22,mosi=21,cs=18,rst=23)

print("Bring TAG closer...")
print("")


while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            print("CARD ID: "+str(card))
utime.sleep_ms(500) 