from gpiozero import LED
from time import sleep

led = LED(17)

while True :
    led.on()
    print("On")
    sleep(1)
    led.off()
    print("Off")