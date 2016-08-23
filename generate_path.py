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

path = generate_path(np.array([0.15, 0.15, 0.15]), np.array([-0.1, 0.1, 0.4]), 0.1, 0.01)
translated_path = [ik(my_chain, x) for x in path]
with open("path", "w") as f:
  f.write(str(translated_path))
print("count of path elemets: " + str(len(translated_path)))
