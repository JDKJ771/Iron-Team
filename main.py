#start all files with import machine this is where you will import your libraries
import machine
import time

#create a variable and give it a pin out
led = machine.Pin(23, machine.Pin.OUT)

#yay you created your first variable in python!

#now we are going to turn the pin on wait 5 seconds then turn it off Put in a while true loop
while True:
      led.on()
      time.sleep(5)
      led.off
