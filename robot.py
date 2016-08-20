from time import sleep
import Adafruit_PCA9685
import numpy as np

print("Start robot")
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)
SERVO_0 = 0
SERVO_1 = 1

min_angle = np.array([-90.0, -90.0, -90.0, -90.0, -90.0, -90.0])
max_angle = np.array([90.0, 90.0, 90.0, 90.0, 90.0, 90.0])
diff_angle = np.absolute(min_angle) + np.absolute(max_angle)
zero_angle = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ])

min = np.array([200.0, 200.0 , 200.0, 200.0, 200.0, 200.0])
max = np.array([400.0, 400.0, 400.0, 400.0, 400.0, 400.0])
diff = max - min
current_angles = np.array(zero_angle)

def set_angles(angles):
  global current_angles
  diff_angles = angles - current_angles
  print("change angle by" + str(diff_angles) + " to "+ str(angles))
  steps = np.amax(np.absolute(diff_angles))
  if steps > 0:
    step = (diff_angles) / steps
    #print("step: " + str(step))
    for i in range(0, int(steps)):
      current_angles += step
      set_angles_raw(current_angles)
      sleep(0.01)

def set_angles_raw(angles):
  calc_values = (diff / diff_angle * (angles + np.absolute(min_angle) )) + min
  print("angles: "+ str(angles) + " -> values: " + str(calc_values))
  for servo,value in enumerate(calc_values):
    pwm.set_pwm(servo, 0, int(value))

set_angles_raw(zero_angle)
for i in range(0,20):
  a = input("angles?")
  set_angles(np.array(a))


raw_input("weiter? ")
set_angles(zero_angle)

