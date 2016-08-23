import ikpy
import numpy as np
import sys


def ik(chain, target_vector):
  target_frame = np.eye(4)
  target_frame[:3, 3] = target_vector
  return chain.inverse_kinematics(target_frame).tolist()[1:7]


def generate_path(start_pos, end_pos, velocity):
  diff = end_pos - start_pos

my_chain = ikpy.chain.Chain.from_urdf_file("file1.urdf")

path = [np.array([(0.15 - (0.001* x)), 0.1,  0.1]) for x in range(0, 300)]
translated_path = [ik(my_chain, x) for x in path]
with open("path", "w") as f:
  f.write(str(translated_path))
