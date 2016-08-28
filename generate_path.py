import ikpy
import numpy as np
import sys
from scipy.spatial import distance

def ik(chain, target_vector):
  target_frame =np.array([
             [1  , 0 , 0 , 0],
             [0 , 1 , 0 ,  0.15],
             [0  , 0 , 1 , 0.1],
             [0  , 0 , 0 , 1  ]
             ])
  target_frame[:3, 3] = target_vector
  return chain.inverse_kinematics(target_frame, regularization_parameter=0.1)


def generate_path(start_pos, end_pos, velocity, resolution):
  dist = distance.euclidean(start_pos, end_pos)
  steps = int((dist / velocity) / resolution)
  step = (end_pos - start_pos) / steps
  return [start_pos + (step * x) for x in range(0, steps)]


my_chain = ikpy.chain.Chain.from_urdf_file("file-with-tool.urdf")

def translate_path(start_pos, end_pos, velocity, resolution):
  path = generate_path(np.array(start_pos),np.array(end_pos), velocity,resolution)
  for p in path:
    print(str(ik(my_chain, p).tolist()[1:7])) 

res = 0.0015
translate_path([0, 0.15, 0.2], [-0.2, 0.15, 0.2], 1, res)
