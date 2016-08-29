#!/usr/bin/env python
from time import sleep
import readchar
import numpy as np
import tornado.httpclient
import urllib
import ikpy
import numpy as np
import sys
import ikpy.geometry_utils

my_chain = ikpy.chain.Chain.from_urdf_file("file-with-tool2.urdf")

http_client = tornado.httpclient.HTTPClient()

def cmd(cmd, data):
  d = { 'cmd': cmd, 'data': str(data)}
  http_client.fetch(tornado.httpclient.HTTPRequest(url="http://pi:9999/cmd",method="PUT", headers={"Content-Type":       "application/x-www-form-urlencoded"},body=urllib.urlencode(d)))

def change_angles(angles):
  cmd("ca", angles)
def set_angles(angles):
  cmd("sa", angles)
def reset():
  cmd("rs", "")

print("Start robot")
exit = False
step = 0.015
while not exit:
  a = readchar.readchar()
  if a == 'x':
    exit = True
  else:
    if a == 'k':
      target = input("target:")
      rot = [
          [0, -1, 0],
          [1, 0, 0],
          [0, 0, 1]]
      target_frame = ikpy.geometry_utils.to_transformation_matrix( target, rot)
      values = my_chain.inverse_kinematics(target_frame, regularization_parameter=0.1).tolist()[1:7]
      print(str(values))
      set_angles(values)
      exit_k = False
      while not exit_k:
        b = readchar.readchar()
        k_step = 0.002
        add = [0,0,0]
        if b == 'q':
          add = [k_step, 0 , 0] 
        if b == 'a':
          add = [-k_step, 0 , 0] 
        if b == 'w':
          add = [0,k_step,  0] 
        if b == 's':
          add = [0, -k_step, 0] 
        if b == 'e':
          add = [0,0,k_step] 
        if b == 'd':
          add = [0,0, -k_step] 
        if b == 'x':
          exit_k=True 
        target = np.array(target) + np.array(add)
        target_frame = ikpy.geometry_utils.to_transformation_matrix( target, rot)
        values = my_chain.inverse_kinematics(target_frame, regularization_parameter=0.05).tolist()[1:7]
        print(str(target) + " -> " + str(values))
        set_angles(values)
       
    if a == 'p':
      p = input("New pos:")
      set_angles(p)
    if a == 'n':
      path = raw_input("file with path:")
      with open(path, "r") as f:
        lines = [eval(line) for line in f]
      robot.move_path(lines)
    if a == 'c':
      reset()
reset()

