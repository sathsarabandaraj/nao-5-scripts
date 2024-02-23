import argparse
from naoqi import ALProxy
import time
import sys

robot_ip = "192.168.1.18"
robot_port = 9559

aud = ALProxy("ALAudioPlayer", robot_ip, robot_port)

aud.post.playFile("/home/nao/music/fastx.mp3", 0.5, 0.0)
