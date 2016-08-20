from time import sleep
import readchar
import numpy as np
import robot_arm as ra

print("reset robot")
robot = ra.Robot(50)
robot.reset()

