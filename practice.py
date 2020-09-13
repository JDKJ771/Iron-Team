import machine


Blue=machine.pin(21,machine.pin.OUT)

Leaf=machine.pin(22.machine.pin.IN)

red=machine.pin(23,machine.pin.OUT)

lead=machine.pin(19,machine.pin.IN)

Leaf.value()
lead.value()

while True:
if leaf() ==1:
 Leaf.OFF()
else:
 Leaf.on()
 if red()==1:
     Blue.off()
