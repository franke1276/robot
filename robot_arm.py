from time import sleep
import readchar
import Adafruit_PCA9685
import numpy as np

class Robot():
  freq = None
  current = np.array([300,300,300,300,300,300])
  pwm = None

  def __init__(self, freq):
    self.freq = freq
    self.pwm = Adafruit_PCA9685.PCA9685()
    self.pwm.set_pwm_freq(50)
    self.__set_angles_raw(self.current)
  def reset(self):
    self.set_angles(np.array([300,300,300,300,300,300]))
  def current_pos(self):
    return self.current
  def __gtOrLtOrEq(self, z):
    if z > 0:
      return 1
    if z < 0:
      return -1
    return 0
  def set_angles(self,angles):
    while not np.array_equal(angles, self.current):
      diff = angles - self.current
      step = [self.__gtOrLtOrEq(x) for x in diff]
      print("change angle by" + str(diff) + " to "+ str(angles))
      print("step: " + str(step))
      self.current += step
      self.__set_angles_raw(self.current)
      sleep(0.01)

  def __set_angles_raw(self, values):
    print("set values: " + str(values))
    for servo,value in enumerate(values):
      self.pwm.set_pwm(servo, 0, int(value))

