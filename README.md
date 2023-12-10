# R2D2 2.0 
Advanced Embedded Systems Project Fall 2023

# Overview
This is the repository for development done on an R2D2 robot using a Nvidia Jetson Nano. The R2D2 robot was originally from a hobby project that fans of the Star Wars universe could build and put together themselves. However, all of the electronics and internal software came as is, with little to no ability to make your own hardware or software improvements. Our team then took apart the existing robot and rebuilt his insides to improve existing functionality and expand his capabilities, you can find the repository here :https://github.com/Myapi314/R2D2Project.

I upgraded the main hardware and redesigned the complete software. I continued using ROS2 to run the bulk of the project on the main computer. The project consists in 5 different nodes/files
* voice_publisher: It handles the user voice input and writes to an arduino nano and to the voice subscriber.
* subscriber: It receives the user input voice and decides what sounds and videos to play
* arduino code: It handles the LEDs and Projector.
* server: It runs the r2d2 server and receives the data that controls the direction and speed of the wheels motors.
* webstreaming: It creates the code to run OpenCV motion detection and a websocket connection to send image in real time of what R2D2 is seeing to a webpage where it can be watched and controlled.
* index.html: It creates a webpage to display the data from webstreaming.py and creates a joystick to control the R2D2 through wifi.

The arduino nano is used only to controls LEDs which communicated with our robot via a serial USB connection and the turning on and off of the Projector.

# Development Environment
NVIDIA Jetson Nano Developer Kit

Ubuntu 20.04.6 LTS

ROS2 Foxy

ArduinoIDE, Visual Studio Code, Python, OpenCv

# Hardware
Camera, projector, mic, motor drivers


# Resources
* https://pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/
* https://www.instructables.com/Making-a-Joystick-With-HTML-pure-JavaScript/
* https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html
* https://www.theconstructsim.com/create-python-publisher-ros2/
* https://chat.openai.com
* https://howtomechatronics.com/tutorials/arduino/arduino-dc-motor-control-tutorial-l298n-pwm-h-bridge
* https://forums.developer.nvidia.com/t/how-do-i-use-pwm-on-jetson-nano/72595/5
* https://forums.developer.nvidia.com/t/how-to-use-configure-pwm/108780/2
