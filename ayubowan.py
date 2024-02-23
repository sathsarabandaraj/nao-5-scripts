import argparse
from naoqi import ALProxy
import time

motion = None

def main(robot_IP, robot_PORT=9559):
    global motion

    motion = ALProxy('ALMotion', robot_IP, robot_PORT)
    tts = ALProxy('ALTextToSpeech', robot_IP, robot_PORT)

    text_ayubowan = 'Ayuu boowaan'
    text_wanakkam = 'Wanakkam'
    text_welcome = 'Welcome'

    # motion.rest()
    RestArm()
    motion.wakeUp()
    time.sleep(1)

    LArmInit()
    RArmInit()
    HipMove(-0.5)
    time.sleep(1)
    tts.say(text_ayubowan)
    time.sleep(0.5)
    tts.say(text_wanakkam)
    time.sleep(0.5)
    tts.say(text_welcome)
    # time.sleep(0.5)
    HipMove(-0.2)
    RestArm()
    CloseHands()
    time.sleep(3)

    # motion.rest()

def HipMove(rad):
    motion.setAngles('LHipYawPitch', rad, 0.1)

def LArmInit():
	motion.setAngles('LShoulderPitch', 0.7, 0.2)
	motion.setAngles('LShoulderRoll', -0.3, 0.2)
	motion.setAngles('LElbowYaw', -1.0, 0.2)
	motion.setAngles('LElbowRoll', -1.5, 0.2)
	# motion.setAngles('LWristYaw', 0, 0.2)
	motion.setAngles('LHand', 0.7, 0.2)
     
def RArmInit():
    motion.setAngles('RShoulderPitch', 0.7, 0.2)
    motion.setAngles('RShoulderRoll', 0.3, 0.2)
    motion.setAngles('RElbowYaw', 1.0, 0.2)
    motion.setAngles('RElbowRoll', 1.5, 0.2)
    motion.setAngles('RHand', 0.7, 0.2)

def CloseHands():
    motion.setAngles('LHand', 0, 0.2)
    motion.setAngles('RHand' , 0, 0.2)

def RestArm():
    motion.setAngles('LShoulderPitch', 1.5, 0.2)
    motion.setAngles('LShoulderRoll', 0, 0.2)
    motion.setAngles('LElbowYaw', -1.0, 0.2)
    motion.setAngles('LElbowRoll', 0, 0.2)

    motion.setAngles('RShoulderPitch', 1.5, 0.2)
    motion.setAngles('RShoulderRoll', 0, 0.2)
    motion.setAngles('RElbowYaw', 1.0, 0.2)
    motion.setAngles('RElbowRoll', 0, 0.2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.18", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
	
    main(args.ip, args.port)