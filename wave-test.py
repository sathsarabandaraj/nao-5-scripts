import argparse
from naoqi import ALProxy
import time

motion = None
def main(robot_IP, robot_PORT=9559):
    global motion
    motion = ALProxy('ALMotion', robot_IP, robot_PORT)
    # motion.rest()
    # motion.wakeUp()
    #WaveL()
    for i in range(5):  # Loop from 0 to 4 (inclusive)
        time.sleep(1)
        WaveR()
        time.sleep(1)
        WaveL()
    RestArm()

def WaveL():
    motion.setAngles('RShoulderPitch', -1.5, 0.2)
    motion.setAngles('RShoulderRoll', -0.9, 0.2)
    motion.setAngles('RElbowYaw', 1.4, 0.2)
    motion.setAngles('RElbowRoll', 0.55, 0.2)
    motion.setAngles('RWristYaw', -1.0, 0.2)
    motion.setAngles('RHand', 1, 0.2)

def WaveR():
    motion.setAngles('RShoulderPitch', -1.5, 0.2)
    motion.setAngles('RShoulderRoll', -0, 0.2)
    motion.setAngles('RElbowYaw', 1.4, 0.2)
    motion.setAngles('RElbowRoll', 0.55, 0.2)
    motion.setAngles('RWristYaw', -1.5, 0.2)
    motion.setAngles('RHand', 1, 0.2)


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
    parser.add_argument("--ip", type=str, default="nao.local", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
	
    main(args.ip, args.port)