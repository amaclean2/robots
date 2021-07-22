import RPi.GPIO as GPIO
import pigpio
import argparse
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pi = pigpio.pi()

ESC_GPIO = 13

parser = argparse.ArgumentParser()

parser.add_argument("--calibrate", help="set the calibration mode of the esc")
args = parser.parse_args()

print("calibrate ", args.calibrate)

if args.calibrate == "c" :
    # calibrating the ESC
    pi.set_servo_pulsewidth(ESC_GPIO, 2000)
    print("calibrate_hi")
    sleep(2)
    pi.set_servo_pulsewidth(ESC_GPIO, 1000)
    print("calibrate_lo")
    sleep(2)

elif args.calibrate == "t" :
    for speed in range(6) :
        pi.set_servo_pulsewidth(ESC_GPIO, speed * 1000 / 7 + 1000)
        print("running speed: ", speed * 1000 / 7 + 1000)
        sleep(2)
        pi.set_servo_pulsewidth(ESC_GPIO, 0)
        sleep(1)

else :
    speed = 3.8
    pi.set_servo_pulsewidth(ESC_GPIO, speed * 1000 / 7 + 1000)
    print("testing speed: ", speed)
    sleep(2)
    pi.set_servo_pulsewidth(ESC_GPIO, speed * 1000 / 7 + 1000)
    print("testing speed: ", speed)
    sleep(2)

# shutting everything down
pi.set_servo_pulsewidth(ESC_GPIO, 0)
pi.stop()
print("done")
