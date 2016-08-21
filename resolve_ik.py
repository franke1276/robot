import ikpy
import numpy as np
from ikpy import plot_utils
import matplotlib.pyplot as plt


my_chain = ikpy.chain.Chain.from_urdf_file("file.urdf")

target_vector = [ 0.15, 0.15, 0.2]
target_frame = np.eye(4)
target_frame[:3, 3] = target_vector

print("for " + str(target_vector) + " The angles of each joints are : ", my_chain.inverse_kinematics(target_frame))
#ax = plot_utils.init_3d_figure()
#my_chain.plot(my_chain.inverse_kinematics(target_frame), ax, target=target_vector)
#plt.xlim(-0.1, 0.1)
#plt.ylim(-0.1, 0.1)
#plt.show()
