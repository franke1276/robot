from time import sleep
import readchar
import Adafruit_PCA9685
import numpy as np

print("Start robot")
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)
zero = np.array([300,300,300,300,300,300])

current_angles= np.array(zero)

def set_angles(angles):
  global current_angles
  diff_angles = angles - current_angles
  print("change angle by" + str(diff_angles) + " to "+ str(angles))
  steps = np.amax(np.absolute(diff_angles))
  print("steps: " + str(steps))
  if steps > 0:
    step = (diff_angles) / steps
    for i in range(0, int(steps)):
      current_angles += step
      set_angles_raw(current_angles)
      sleep(0.01)

def set_angles_raw(values):
  print("set values: " + str(values))
  for servo,value in enumerate(values):
    pwm.set_pwm(servo, 0, int(value))

set_angles_raw(zero)
exit = False
while not exit:
  a = readchar.readchar()
  if a == 'x':
    exit = True
  else:
    if a == 'q':
      set_angles(current_angles + np.array([1,0,0,0,0,0]))
    if a == 'a':
      set_angles(current_angles + np.array([-1,0,0,0,0,0]))
    if a == 'w':
      set_angles(current_angles + np.array([0,1,0,0,0,0]))
    if a == 's':
      set_angles(current_angles + np.array([0,-1,0,0,0,0]))
    if a == 'e':
      set_angles(current_angles + np.array([0,0,1,0,0,0]))
    if a == 'd':
      set_angles(current_angles + np.array([0,0,-1,0,0,0]))
    if a == 'r':
      set_angles(current_angles + np.array([0,0,0,1,0,0]))
    if a == 'f':
      set_angles(current_angles + np.array([0,0,0,-1,0,0]))
    if a == 't':
      set_angles(current_angles + np.array([0,0,0,0,1,0]))
    if a == 'g':
      set_angles(current_angles + np.array([0,0,0,0,-1,0]))
    if a == 'y':
      set_angles(current_angles + np.array([0,0,0,0,0,1]))
    if a == 'h':
      set_angles(current_angles + np.array([0,0,0,0,0,-1]))

set_angles(zero)

