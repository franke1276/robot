#!/usr/bin/env python
import ikpy
import numpy as np
from ikpy import plot_utils
import sys

my_chain = ikpy.chain.Chain.from_urdf_file("file-with-tool2.urdf")
target_frame =[
             [0  , -1 , 0 , 0],
             [1 ,   0 , 0 ,  0.2],
             [0  ,  0 , 1 , 0.15],
             [0  , 0 , 0 , 1  ]
             ]
print(str(my_chain.inverse_kinematics(target_frame).tolist()[1:7]))
