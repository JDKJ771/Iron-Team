import machine


IronMan = machine.Pin(12, machine.Pin.OUT)
Button = machine.Pin(22, machine.Pin.IN)


Button.value()

while True:
  if Button() == 1:
        IronMan.off()
  else:
        IronMan.on()
