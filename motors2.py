import RPi.GPIO as GPIO
import pigpio
import sys
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pi = pigpio.pi()

ESC_GPIO = 13

calibrate = 0

if __name__ == "__main__" and len(sys.argv) > 1 :
    calibrate = int(sys.argv[1])

print("calibrate ", calibrate)

if calibrate == 1 :
    # calibrating the ESC
    pi.set_servo_pulsewidth(ESC_GPIO, 2000)
    print("calibrate_hi")
    sleep(2)
    pi.set_servo_pulsewidth(ESC_GPIO, 1000)
    print("calibrate_lo")
    sleep(2)

pi.set_servo_pulsewidth(ESC_GPIO, 2 * 1000 / 7 + 1000)
print("testing speed ", 2)
sleep(1)

# shutting everything down
pi.set_servo_pulsewidth(ESC_GPIO, 0)
pi.stop()
