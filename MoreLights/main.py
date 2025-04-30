import machine
import time

p2 = machine.Pin(2,machine.Pin.OUT) # Built in
p4 = machine.Pin(4,machine.Pin.OUT) # Yellow
p5 = machine.Pin(5,machine.Pin.OUT) # Red

p2.on()

while True:
    print('Hello there')
    p2.off()
    p4.off()
    p5.off()
    time.sleep(1)
    p2.on()
    p4.on()
    p5.on()
    time.sleep(1)
