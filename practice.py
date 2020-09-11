import machine
import time

IronMan =machine.Pin(12, machine.Pin.OUT)

while True:
  IronMan.on()
  time.sleep(6)
  IronMan.off()
  time.sleep(6)
