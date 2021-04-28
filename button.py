from gpiozero import Button
from time import sleep

button = Button(2)

while True :
    print(button.is_active)
    sleep(0.01)