"""
Use a DHT module on my esp32

DHT22   ->  ESP32
+       ->  3V3
out     ->  D33
-       ->  GND
"""

import dht
import machine
import time

d = dht.DHT22(machine.Pin(33))

while True:
    time.sleep(2)
    print('measuring...')

    d.measure()
    print(d.humidity())
    print(d.temperature())
