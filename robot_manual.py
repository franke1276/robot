from time import sleep
import readchar
import numpy as np
import robot_arm_angles as ra

print("Start robot")
robot = ra.Robot(50)
exit = False
step = 0.05
while not exit:
  a = readchar.readchar()
  if a == 'x':
    exit = True
  else:
    if a == 'q':
      robot.change_angles(np.array([step,0,0,0,0,0]))
    if a == 'a':
      robot.change_angles(np.array([-step,0,0,0,0,0]))
    if a == 'w':
      robot.change_angles(np.array([0,step,step,0,0,0]))
    if a == 's':
      robot.change_angles(np.array([0,-step,-step,0,0,0]))
    if a == 'e':
      robot.change_angles(np.array([0,0,step,0,0,0]))
    if a == 'd':
      robot.change_angles(np.array([0,0,-step,0,0,0]))
    if a == 'r':
      robot.change_angles(np.array([0,0,0,step,0,0]))
    if a == 'f':
      robot.change_angles(np.array([0,0,0,-step,0,0]))
    if a == 't':
      robot.change_angles(np.array([0,0,0,0,step,0]))
    if a == 'g':
      robot.change_angles(np.array([0,0,0,0,-step,0]))
    if a == 'y':
      robot.change_angles(np.array([0,0,0,0,0,step]))
    if a == 'h':
      robot.change_angles(np.array([0,0,0,0,0,-step]))
    if a == 'p':
      p = input("New pos:")
      robot.set_angles(np.array(p))
      print("current pos: " + str(robot.current_pos()))
    if a == 'n':
      path = raw_input("file with path:")
      with open(path, "r") as f:
        data = eval(f.read())
        robot.move_path(data)
    if a == 'c':
      robot.reset()
    if a == 'm':
      p = raw_input("Name:")
      print(p + ": " + str(robot.current_pos()))
robot.reset()

