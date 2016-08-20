from time import sleep
import readchar
import numpy as np
import robot_arm_angles as ra

print("Start robot")
robot = ra.Robot(50)
exit = False
while not exit:
  a = input("vector:")
  robot.set_angles(np.array(a))
robot.reset()

