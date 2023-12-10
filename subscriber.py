#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
from playsound import playsound
import pygame
import subprocess
import time

pygame.mixer.init()
#arduino = serial.Serial('/dev/ttyUSB0',115200)
listeningSound = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/R2D2-confusion.wav")
hello_there = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/EasterEggs/general-kenobi.wav")
batman = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/EasterEggs/ImBatman.wav")
cantina = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/EasterEggs/cantina.wav")
chewbacca = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/EasterEggs/chewbacca.wav")
tryIt = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/EasterEggs/do-or-do-not-there-is-no-try.wav")
force= pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/EasterEggs/ForceTheme.wav")
jedi = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/EasterEggs/IamAJedi.wav")
hateYou = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/EasterEggs/i-hate-you!.wav")
mandoSong = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/EasterEggs/mandoSong.wav")
never = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/EasterEggs/never.wav")
yourFather = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/EasterEggs/no-i-am-your-father.wav")
thisIstheWay= pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/EasterEggs/this-is-the-way.wav")
yodaForce = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/EasterEggs/yodaA.wav")
yodaLaugh = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/EasterEggs/(yoda-chuckling).wav")
yodaScream= pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/EasterEggs/yoda-scream.wav")
jarjar = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/Victory.wav")
agree = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/R2D2- Agree.wav")
alert = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/R2D2-alert.wav")
scream = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/R2Scream.wav")
# jarjar = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/ImBatman.wav")
# jarjar = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/ImBatman.wav")
# jarjar = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/ImBatman.wav")
# jarjar = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/ImBatman.wav")
# jarjar = pygame.mixer.Sound("/home/jetson/Desktop/r2d2/sounds/ImBatman.wav")




arduino = serial.Serial('/dev/ttyUSB0',115200)

def play_fullscreen_video(video_path):
    # Build the command to run GStreamer with video and audio
    cmd = ['gst-launch-1.0', 'playbin', 'uri=file://' + video_path]

    # Run the command
    subprocess.call(cmd)


def callback(msg,node):
    node.get_logger().info('Received message: "%s"' % msg.data)
    if msg.data in ("R2", "R2-D2", "hey R2-D2"):
        print(msg.data)
        listeningSound.play()
    elif(msg.data == "hello there"):
        print(msg.data)
        hello_there.play()
    elif(msg.data == "who are you"):
        print(msg.data)
        batman.play()
    elif(msg.data == "Cantina"):
        print(msg.data)
        cantina.play()
    elif(msg.data == "try it"):
        print(msg.data)
        tryIt.play()
    elif(msg.data == "wookie"):
        print(msg.data)
        chewbacca.play()
    elif(msg.data == "what is the force"):
        print(msg.data)
        yodaForce.play()
    elif(msg.data == "force theme"):
        print(msg.data)
        force.play()
    elif(msg.data == "Jedi"):
        print(msg.data)
        jedi.play()
    elif(msg.data == "scream"):
        print(msg.data)
        scream.play()
    elif(msg.data == "I love you"):
        print(msg.data)
        hateYou.play()
    elif(msg.data == "Mandalorian"):
        print(msg.data)
        mandoSong.play()
    elif(msg.data == "this is the way"):
        print(msg.data)
        thisIstheWay.play()
    elif(msg.data == "hit it"):
        print(msg.data)
        never.play()
    elif(msg.data == "you killed my father"):
        print(msg.data)
        yourFather.play()
    elif(msg.data == "Yoda"):
        print(msg.data)
        yodaScream.play()
    elif(msg.data == "laugh"):
        print(msg.data)
        yodaLaugh.play()
    elif(msg.data == "victory"):
        print(msg.data)
        jarjar.play()
    elif(msg.data == "agree"):
        print(msg.data)
        agree.play()
    elif(msg.data == "alert"):
        print(msg.data)
        alert.play()
    elif(msg.data == "help me"):
        # arduino.write(("ON\n").encode())
        # time.sleep(12)
        print(msg.data)
        play_fullscreen_video("/home/jetson/Desktop/r2d2/videos/leia.mp4")
    elif(msg.data == "projector off"):
        arduino.write(("OFF\n").encode())
    elif(msg.data == "play video"):
        play_fullscreen_video("/home/jetson/Desktop/r2d2/videos/leia-only-hope.mp4")

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('sos_subscriber')
    subscription = node.create_subscription(String, 'my_topic', lambda msg: callback(msg,node),10)
    subscription

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
