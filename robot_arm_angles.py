from time import sleep
import readchar
import Adafruit_PCA9685
import numpy as np

class Robot():
  freq = None
  current = None
  pwm = None
  offset = np.array([335,339,139,200,325,336])
  factor = np.array([113,107,-73,-104,131,-119])

  def __init__(self, freq):
    self.freq = freq
    self.pwm = Adafruit_PCA9685.PCA9685()
    self.pwm.set_pwm_freq(50)
    self.reset()
  def reset(self):
    self.current = self.translate(np.array([0,0,0,0,0,0]))
    self.__set_angles_raw(self.current)
  def current_pos(self):
    return self.current
  def __gtOrLtOrEq(self, z):
    if z > 0:
      return 1
    if z < 0:
      return -1
    return 0
  def translate(self, angles):
    return (angles * self.factor) + self.offset
  def set_angles(self,angles):
    translated_angles = self.translate(angles).astype(int)
    while not np.array_equal(translated_angles, self.current):
      print("translated_angles: " + str(translated_angles) + " self.current: " + str(self.current))
      diff = translated_angles - self.current
      step = [self.__gtOrLtOrEq(x) for x in diff]
      #print("change angle by" + str(diff) + " to "+ str(translated_angles)+ " angeles: " + str(angles))
      #print("step: " + str(step))
      self.current += step
      self.__set_angles_raw(self.current)
      sleep(0.002)

  def __set_angles_raw(self, values):
    #print("set values: " + str(values))
    for servo,value in enumerate(values):
      self.pwm.set_pwm(servo, 0, int(value))

