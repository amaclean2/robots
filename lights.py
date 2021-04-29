from gpiozero import LED
from time import sleep

led = LED(17)

while True :
    led.on()
    print("On")
    sleep(0.01)
    led.off()
    print("Off")
    sleep(0.01)