import ikpy
import numpy as np
from ikpy import plot_utils
import sys

my_chain = ikpy.chain.Chain.from_urdf_file("file-with-tool.urdf")
list = [float(x) for x in sys.argv[1:4]]
print(list)
target_vector = list
target_frame = np.eye(4)
target_frame[:3, 3] = target_vector
#print(str(my_chain.inverse_kinematics(target_frame).tolist()[1:7]))
print(str(my_chain.inverse_kinematics([
                               [1, 0, 0, 0.1],
                               [0, 0.1, -0.7, 0.1],
                               [0, 0.7, 0.7, 0.1],
                               [0, 0, 0, 1]]).tolist()[1:7]))
