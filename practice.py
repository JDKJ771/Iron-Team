#Nellie
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

   
   #Jed
   
   import machine

blue = machine.Pin(23, machine.Pin.OUT)
green = machine.Pin(21, machine.Pin.OUT)
redbutton = machine.Pin(22, machine.Pin.IN)
bluebutton = machine.Pin(19, machine.Pin.IN)

redbutton.value()
bluebutton.value()


while True:
  if redbutton() == 1:
    blue.off()
    
  else:
    blue.on()
    
  if bluebutton() == 1:
    green.off()
    
  else:
    green.on()
