from gpiozero import LED,Button
from time import sleep

led = LED(17)
button = Button(2)

while True :
    if (button.is_active) :
        led.on()
    else
        led.off()
    sleep(0.01)