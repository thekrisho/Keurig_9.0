# Import Library 
import CHIP_IO.GPIO as GPIO
import time


# Setup Pins
print (" ")
print ("Keurig 2.0 HACKED")
print ("Please wait...")
GPIO.setup("GPIO4", GPIO.OUT) #XIO-P5 Handle
GPIO.setup("GPIO6", GPIO.OUT) #XIO-P7 Button
GPIO.output("GPIO4", GPIO.HIGH)
GPIO.output("GPIO6", GPIO.HIGH)
time.sleep(1)

# Start Brew Sequence
print ("Brewing")
GPIO.output("GPIO4", GPIO.LOW)
time.sleep(1)
print ("Handle Activated")
GPIO.output("GPIO4", GPIO.HIGH)
time.sleep(4)

print ("Button Activated")
GPIO.output("GPIO6", GPIO.LOW)
time.sleep(1)

GPIO.output("GPIO4", GPIO.HIGH)
GPIO.output("GPIO6", GPIO.HIGH)
time.sleep(1)

print ("All Done")
print ("Thanks :)")
print (" ")

GPIO.cleanup()
GPIO.cleanup()

#import subprocess
#subprocess.call("./clean")
