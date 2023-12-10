# #!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import speech_recognition as sr
import serial
import pygame
import time



arduino = serial.Serial('/dev/ttyUSB0',115200)

class VoiceCommandPublisher(Node):

    def __init__(self):
        super().__init__('voice_publisher')
        self.publisher = self.create_publisher(String, 'my_topic', 10)

    def main(self):
        while True:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Say R2-D2")
                arduino.write(("Listening").encode())
                time.sleep(1)
                print("listening")
                recognizer.adjust_for_ambient_noise(source)
                #audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
                audio = recognizer.record(source,2,None)

            try:
                transcription = recognizer.recognize_google(audio)
                if transcription in ["R2", "R2-D2", "hey R2-D2"]:
                    arduino.write(("Speak").encode())
                    print("Say Something...")
                    msg = String()
                    msg.data = "R2-D2"
                    self.publisher.publish(msg)
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        recognizer.adjust_for_ambient_noise(source)
                        audio = recognizer.listen(source, phrase_time_limit=3, timeout=10)
                        text = recognizer.recognize_google(audio, language="en-US")
                        msg = String()
                        msg.data = text
                        self.publisher.publish(msg)
                        self.get_logger().info('Published voice')
                        print(text)
                else:
                    arduino.write(("Did not listen").encode())   
            except sr.WaitTimeoutError:
                print("No speech detected within the last 2 seconds.")
            except sr.UnknownValueError:
                print("Google Web Speech API could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Web Speech API; {0}".format(e))

    def publish_voice_command(self, text):
        msg = String()
        msg.data = text
        self.publisher.publish(msg)
        self.get_logger().info('Published voice command: %s' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = VoiceCommandPublisher()
    try:
        node.main()
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
  