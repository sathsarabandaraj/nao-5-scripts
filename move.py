from naoqi import ALProxy
motion = ALProxy("ALMotion", "192.168.1.18", 9559)
motion.moveInit()
motion.moveTo(1, 0, 0)