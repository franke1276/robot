#!/usr/bin/env python
import tornado.ioloop
import tornado.web
from time import sleep
import readchar
import numpy as np
import robot_arm_angles as ra
import urllib
robot = ra.Robot(50)

class MainHandler(tornado.web.RequestHandler):
  def put(self):
    cmd = self.get_argument("cmd", "-")
    data = self.get_argument("data", "-")
    print("cmd: " + cmd + ", data: " + data)
    if cmd == "ca":
      angles = eval(data)
      robot.change_angles(np.array(angles))
      self.write("OK")
    if cmd == "rs":
      robot.reset()
      self.write("OK")
    if cmd == "sa":
      angles = eval(data)
      robot.set_angles(np.array(angles))
      self.write("OK")

  def get(self):
    self.write(str(robot.current_pos()))

def make_app():
    return tornado.web.Application([
        (r"/cmd", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()
