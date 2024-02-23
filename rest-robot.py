import argparse
from naoqi import ALProxy

motion = None

def main(robot_IP, robot_PORT=9559):
    global motion

    motion = ALProxy('ALMotion', robot_IP, robot_PORT)

    motion.rest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="nao.local", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
	
    main(args.ip, args.port)