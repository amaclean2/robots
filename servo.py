import RPi.GPIO as GPIO
import argparse
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

SEREVO_GPIO = 11

GPIO.setup(SEREVO_GPIO, GPIO.OUT)
servo = GPIO.PWM(SEREVO_GPIO, 50)

parser = argparse.ArgumentParser()

parser.add_argument("--test", help="set the calibration mode of the esc")
args = parser.parse_args()

if args.test == "test" :
    servo.start(0)
    print("waiting")
    sleep(2)

    print("rotating")

    duty = 2


    while duty <= 12 :
        servo.ChangeDutyCycle(duty)
        sleep(2)
        duty += 1

    sleep(2)

    print("turning back to 90")
    servo.ChangeDutyCycle(7)
    sleep(2)

    print("turning back to 0")
    servo.ChangeDutyCycle(2)
    sleep(0.5)
    servo.ChangeDutyCycle(0)

else :
    servo.start(0)
    servo.ChangeDutyCycle(7)
    sleep(0.3)
    servo.ChangeDutyCycle(0)
    sleep(0.7)

    servo.ChangeDutyCycle(8.5)
    sleep(0.3)
    servo.ChangeDutyCycle(0)
    sleep(0.7)

    # servo.ChangeDutyCycle(5.5)
    # sleep(0.3)
    # servo.ChangeDutyCycle(0)
    # sleep(0.7)

    # servo.ChangeDutyCycle(7)
    # sleep(0.5)
    # servo.ChangeDutyCycle(0)

servo.stop()
GPIO.cleanup()
print("done")
