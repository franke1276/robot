import ikpy
import numpy as np
import sys
from scipy.spatial import distance

def ik(chain, target_vector):
  target_frame = np.eye(4)
  target_frame[:3, 3] = target_vector
  return chain.inverse_kinematics(target_frame).tolist()[1:7]


def generate_path(start_pos, end_pos, velocity, resolution):
  dist = distance.euclidean(start_pos, end_pos)
  steps = int((dist / velocity) / resolution)
  step = (end_pos - start_pos) / steps
  return [start_pos + (step * x) for x in range(0, steps)]


my_chain = ikpy.chain.Chain.from_urdf_file("file1.urdf")

def translate_path(start_pos, end_pos, velocity, resolution):
  path = generate_path(np.array(start_pos),np.array(end_pos), velocity,resolution)
  translated_path = [ik(my_chain, x) for x in path]
  for p in translated_path:
   print(str(p)) 

res = 0.0015
translate_path([0, 0.196, 0.245], [0.1, 0.1, 0.1], 1, res)
translate_path([0.1, 0.1, 0.1], [-0.1, 0.1, 0.1], 1, res)
translate_path([-0.1, 0.1, 0.1], [0, 0.25, 0.1], 1, res)
translate_path([0, 0.25, 0.1], [0.1, 0.1, 0.1], 1, res)
translate_path( [0.1, 0.1, 0.1],[0, 0.196, 0.245], 1, res)
