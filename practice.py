import machine
import time

IronMan =machine.Pin(12, machine.Pin.OUT)
Button=machine.Pin(4, machine.Pin.IN)


while True:
  if Button==0:
    IronMan.on()
  else:
    IronMan.off()
