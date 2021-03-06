#!/usr/bin/env python
from time import sleep
import readchar
import numpy as np
import robot_arm_angles as ra
import tornado.httpclient
http_client = tornado.httpclient.HTTPClient()

response = http_client.fetch("http://pi:9999/cmd")
def cmd(cmd, data):
  http_client.fetch(HTTPRequest(url="http://pi:9999/cmd",method="PUT", body="cmd="+cmd+"&data=" + str(data)))

def change_angles(angles):
  cmd("ca", angles)
def set_angles(angles):
  cmd("sa", angles)

print("Start robot")
robot = ra.Robot(50)
exit = False
step = 0.0015
while not exit:
  a = readchar.readchar()
  if a == 'x':
    exit = True
  else:
    if a == 'q':
      change_angles([step,0,0,0,0,0])
    if a == 'a':
      change_angles([-step,0,0,0,0,0])
    if a == 'w':
      change_angles([0,step,step,0,0,0])
    if a == 's':
      change_angles([0,-step,-step,0,0,0])
    if a == 'e':
      change_angles([0,0,step,0,0,0])
    if a == 'd':
      change_angles([0,0,-step,0,0,0])
    if a == 'r':
      change_angles([0,0,0,step,0,0])
    if a == 'f':
      change_angles([0,0,0,-step,0,0])
    if a == 't':
      change_angles([0,0,0,0,step,0])
    if a == 'g':
      change_angles([0,0,0,0,-step,0])
    if a == 'y':
      change_angles([0,0,0,0,0,step])
    if a == 'h':
      change_angles([0,0,0,0,0,-step])
    if a == 'p':
      p = input("New pos:")
      set_angles(p)
    if a == 'n':
      path = raw_input("file with path:")
      with open(path, "r") as f:
        lines = [eval(line) for line in f]
      robot.move_path(lines)
    if a == 'c':
      robot.reset()
    if a == 'm':
      p = raw_input("Name:")
      print(p + ": " + str(robot.current_pos()))
robot.reset()

