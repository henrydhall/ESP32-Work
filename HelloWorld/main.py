import machine
import time

p2 = machine.Pin(2,machine.Pin.OUT) #com
p2.on()

while True:
    p2.off()
    time.sleep(1)
    p2.on()
    time.sleep(1)
