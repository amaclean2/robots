import RPi.GPIO as GPIO
import pigpio
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pi = pigpio.pi()

ESC_GPIO = 13
pi.set_servo_pulsewidth(ESC_GPIO, 2000)
sleep(2)
pi.set_servo_pulsewidth(ESC_GPIO, 1000)
sleep(2)

for speed in range(6) :
    pi.set_servo_pulsewidth(ESC_GPIO, speed * 1000 / 7 + 1000)
    sleep(2)

pi.set_servo_pulsewidth(ESC_GPIO, 0)
pi.stop()
