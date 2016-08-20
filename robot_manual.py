from time import sleep
import readchar
import numpy as np
import robot_arm as ra

print("Start robot")
robot = ra.Robot(50)
exit = False
while not exit:
  a = readchar.readchar()
  if a == 'x':
    exit = True
  else:
    if a == 'q':
      robot.set_angles(robot.current_pos() + np.array([1,0,0,0,0,0]))
    if a == 'a':
      robot.set_angles(robot.current_pos() + np.array([-1,0,0,0,0,0]))
    if a == 'w':
      robot.set_angles(robot.current_pos() + np.array([0,1,0,0,0,0]))
    if a == 's':
      robot.set_angles(robot.current_pos() + np.array([0,-1,0,0,0,0]))
    if a == 'e':
      robot.set_angles(robot.current_pos() + np.array([0,0,1,0,0,0]))
    if a == 'd':
      robot.set_angles(robot.current_pos() + np.array([0,0,-1,0,0,0]))
    if a == 'r':
      robot.set_angles(robot.current_pos() + np.array([0,0,0,1,0,0]))
    if a == 'f':
      robot.set_angles(robot.current_pos() + np.array([0,0,0,-1,0,0]))
    if a == 't':
      robot.set_angles(robot.current_pos() + np.array([0,0,0,0,1,0]))
    if a == 'g':
      robot.set_angles(robot.current_pos() + np.array([0,0,0,0,-1,0]))
    if a == 'y':
      robot.set_angles(robot.current_pos() + np.array([0,0,0,0,0,1]))
    if a == 'h':
      robot.set_angles(robot.current_pos() + np.array([0,0,0,0,0,-1]))
    if a == 'm':
      p = raw_input("Name:")
      print(p + ": " + str(robot.current_pos()))
robot.reset()

