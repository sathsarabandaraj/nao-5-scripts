import argparse
from naoqi import ALProxy
import time

motion = None
def main(robot_IP, robot_PORT=9559):
    global motion
    motion = ALProxy('ALMotion', robot_IP, robot_PORT)
    motion.rest()
    motion.wakeUp()
    
    # time.sleep(1)
    # RArmFist()
    # time.sleep(1)
    # RestArm()
    RArm()
    LArm()


def RArm():
    motion.setAngles('RShoulderPitch',-1.1, 0.4)
    motion.setAngles('RShoulderRoll', -1.3, 0.4)
    motion.setAngles('RElbowYaw', 1.0, 0.4)
    motion.setAngles('RElbowRoll', 0.0, 0.4)
    motion.setAngles('RWristYaw', -1.2, 0.4)
    motion.setAngles('RHand', 0.7, 0.4)

def LArm():
    motion.setAngles('LShoulderPitch',0.3, 0.4)
    motion.setAngles('LShoulderRoll', 0.0, 0.4)
    motion.setAngles('LElbowYaw', -0.4, 0.4)
    motion.setAngles('LElbowRoll', -1.5, 0.4)
    motion.setAngles('LWristYaw', -0.0, 0.4)
    motion.setAngles('LHand', 0.4, 0.4)

def RestArm():
    motion.setAngles('LShoulderPitch', 1.5, 0.2)
    motion.setAngles('LShoulderRoll', 0, 0.2)
    motion.setAngles('LElbowYaw', -1.0, 0.2)
    motion.setAngles('LElbowRoll', 0, 0.2)    
    motion.setAngles('LWristYaw', -0.4, 0.2)
    motion.setAngles('LHand', 0.0, 0.2)

    motion.setAngles('RShoulderPitch', 1.5, 0.2)
    motion.setAngles('RShoulderRoll', 0, 0.2)
    motion.setAngles('RElbowYaw', 1.0, 0.2)
    motion.setAngles('RElbowRoll', 0, 0.2)
    motion.setAngles('RWristYaw', 0.4, 0.2)
    motion.setAngles('RHand', 0.0, 0.2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.33 ", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
	
    main(args.ip, args.port)