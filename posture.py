from naoqi import ALProxy

robot_ip = "192.168.1.18"
robot_port = 9559

postureProxy = ALProxy("ALRobotPosture", robot_ip, robot_port)

postureProxy.goToPosture("Sit", 1.0)

