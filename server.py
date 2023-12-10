import asyncio
import websockets
import json
import Jetson.GPIO as GPIO

#D2 IN1 12
#D3 ENA 13 
#D4 IN2 11                                                  
#D5 ENB 15
#D7 IN3 16
#D8 IN4 18

LF_PIN = 12        # LEFT FORWARD - IN1
LB_PIN = 11        # LEFT BACKWARD - IN2
RF_PIN = 16        # RIGHT FORWARD - IN3
RB_PIN = 18        # RIGHT BACKWARD - IN4

LEFT_PWM_PIN = 32  # LEFT SPEED - ENA
RIGHT_PWM_PIN = 33 # RIGHT SPEED - ENB
R_H = 15 #head right brown
L_H = 19 #head left green 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(R_H,GPIO.OUT)
GPIO.setup(L_H,GPIO.OUT)
GPIO.setup(LEFT_PWM_PIN, GPIO.OUT)
GPIO.setup(LF_PIN, GPIO.OUT)
GPIO.setup(LB_PIN, GPIO.OUT)
pw1 = GPIO.PWM(LEFT_PWM_PIN,300)
pw1.start(0)

GPIO.setup(RIGHT_PWM_PIN, GPIO.OUT)
GPIO.setup(RF_PIN, GPIO.OUT)
GPIO.setup(RB_PIN, GPIO.OUT)
pw2 = GPIO.PWM(RIGHT_PWM_PIN,300)
pw2.start(0)

def changeSpeed(speed,y,x):
    if x < 0:
        newSpeed = int(speed + x/2)
        if newSpeed >= 0 or newSpeed <=100:
            # print(newSpeed)
            pw1.ChangeDutyCycle(newSpeed)
            pw2.ChangeDutyCycle(speed)
    if x > 0:
        newSpeed = int(speed - x/2)
        # print(newSpeed)
        if newSpeed >= 0 or newSpeed <=100:
            pw1.ChangeDutyCycle(speed)
            pw2.ChangeDutyCycle(newSpeed)
    if x == 0:
        pw1.ChangeDutyCycle(speed)
        pw2.ChangeDutyCycle(speed)

    if y > 0:
        #if Joystick pointing up
        GPIO.output(RF_PIN,GPIO.HIGH)
        GPIO.output(LF_PIN,GPIO.HIGH)
        GPIO.output(RB_PIN,GPIO.LOW)
        GPIO.output(LB_PIN,GPIO.LOW)
    if y < 0:
        #if Joystick pointing down
        GPIO.output(RF_PIN,GPIO.LOW)
        GPIO.output(LF_PIN,GPIO.LOW)
        GPIO.output(RB_PIN,GPIO.HIGH)
        GPIO.output(LB_PIN,GPIO.HIGH)
  
async def handle_message(websocket, path):
    async for message in websocket:
        try:
            data_dict = json.loads(message)
            # print(data_dict['speed'])
            #print(data_dict['y'])
            #print(data_dict['x'])
            changeSpeed(int(data_dict['speed']), int(data_dict['y']), int(data_dict['x']))
            
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)

if __name__ == "__main__":
    start_server = websockets.serve(handle_message, "10.244.59.68", 8765) 
    # start_server = websockets.serve(handle_message, "10.34.2.2", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
