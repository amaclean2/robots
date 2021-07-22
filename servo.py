import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

SEREVO_GPIO = 11

GPIO.setup(SEREVO_GPIO, GPIO.OUT)
servo = GPIO.PWM(SEREVO_GPIO, 50)

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

servo.stop()
GPIO.cleanup()
print("done")