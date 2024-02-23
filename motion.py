import time
import almath
# import argparse
from naoqi import ALProxy

angle = 0.0

motionProxy = ALProxy("ALMotion", "nao.local", 9559)

#set stiffness
motionProxy.setStiffnesses("Head", 1.0)

names = "HeadPitch"
angles = angle*almath.TO_RAD
fractionMaxSpeed = 0.1
motionProxy.setAngles(names, angles, fractionMaxSpeed)

time.sleep(3.0)
motionProxy.setStiffnesses("Head", 0.0)