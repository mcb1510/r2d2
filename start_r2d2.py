# import required module
from playsound import playsound
import Jetson.GPIO as GPIO
import time
GPIO.setwarnings(False)
IN3 = 15 #head right brown
IN4 = 19 #head left green 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)

playsound("/home/jetson/Desktop/sounds/R2D2idea.wav")
#head goes right
GPIO.output(IN3,GPIO.HIGH)
GPIO.output(IN4,GPIO.LOW)
time.sleep(1)
#head goes left
GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.HIGH)
time.sleep(1.5)
#head to the middle
GPIO.output(IN4, GPIO.LOW)
GPIO.output(IN3,GPIO.HIGH)
time.sleep(0.7)
GPIO.output(IN3,GPIO.LOW)


