from time import sleep
import readchar
import numpy as np
import robot_arm as ra

print("Start robot")
robot = ra.Robot(50)
robot.set_angles(np.array([277,251,243,375,250,345]))
sleep(2)
robot.set_angles(np.array([277,212,265,375,269,345]))
sleep(5)
robot.set_angles(np.array([277,251,243,375,250,345]))
sleep(2)
robot.set_angles(np.array([387,270,267,375,276,345]))
sleep(2)
robot.set_angles(np.array([387,224,298,375,294,345]))
sleep(5)
robot.set_angles(np.array([387,270,267,375,276,345]))
sleep(5)
robot.reset()

