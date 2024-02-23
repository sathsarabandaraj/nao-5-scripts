from naoqi import ALProxy

robot_ip = "nao.local"
robot_port = 9559

tts = ALProxy("ALTextToSpeech", robot_ip, robot_port)
batteryProxy = ALProxy("ALBattery", robot_ip, robot_port)

battery_percentage = batteryProxy.getBatteryCharge()

text = "Hello, my battery level is {} percent.".format(battery_percentage)

tts.say(text)