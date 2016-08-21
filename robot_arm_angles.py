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
  current_angles = None
  def __init__(self, freq):
    self.freq = freq
    self.pwm = Adafruit_PCA9685.PCA9685()
    self.pwm.set_pwm_freq(50)
    self.reset()
  def reset(self):
    self.current_angles = np.array([0,0,0,0,0,0])
    self.current = self.translate(self.current_angles)
    self.__set_angles_raw(self.current)
  def current_pos(self):
    return self.current_angles
  def __gtOrLtOrEq(self, z):
    if z > 0:
      return 1
    if z < 0:
      return -1
    return 0
  def translate(self, angles):
    return (angles * self.factor) + self.offset
  def change_angles(self, angles_diff):
    self.set_angles(self.current_pos() + angles_diff)
  def set_angles(self,angles):
    translated_angles = self.translate(angles).astype(int)
    self.current = translated_angles
    self.__set_angles_raw(self.current)
    print("go to: " + str(angles))
#    while not np.array_equal(translated_angles, self.current):
#      diff = translated_angles - self.current
#      step = [self.__gtOrLtOrEq(x) for x in diff]
#      #print("change angle by" + str(diff) + " to "+ str(translated_angles)+ " angeles: " + str(angles))
#      #print("step: " + str(step))
#      self.current += step
#      self.__set_angles_raw(self.current)
#      sleep(0.002)
    self.current_angles = angles

  def __set_angles_raw(self, values):
    #print("set values: " + str(values))
    for servo,value in enumerate(values):
      self.pwm.set_pwm(servo, 0, int(value))

