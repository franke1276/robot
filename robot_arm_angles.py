from time import sleep
import readchar
import Adafruit_PCA9685
import numpy as np

class Robot():
  freq = None
  current = None
  pwm = None
  offset = np.array([329,335,136,185,325,323])
  factor = np.array([113,107,-73,104,-131,119])
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
  def translate(self, angles):
    return (angles * self.factor) + self.offset
  def change_angles(self, angles_diff):
    self.set_angles(self.current_pos() + angles_diff)
  def move_path(self, path):
    for p in path:
      self.set_angles(p)
      sleep(0.015)
  def set_angles(self,angles):
    corrected_angles = np.array(angles)
    corrected_angles[2] = corrected_angles[2] + corrected_angles[1] * 1.3
    translated_angles = self.translate(corrected_angles).astype(int)
    print(str(self.translate((np.array(angles)))))
    self.current = translated_angles
    self.__set_angles_raw(self.current)
    print("go to: " + str(angles))
    self.current_angles = angles

  def __set_angles_raw(self, values):
    #print("set values: " + str(values))
    for servo,value in enumerate(values):
      self.pwm.set_pwm(servo, 0, int(value))

