#!/usr/bin/env python
import ikpy
import numpy as np
import sys

my_chain = ikpy.chain.Chain.from_urdf_file("file-with-tool2.urdf")
target_frame =[
             [0  , -1 , 0 , 0],
             [1 ,   0 , 0 ,  0.24],
             [0  ,  0 , 1 , 0.24],
             [0  , 0 , 0 , 1  ]
             ]
pos1 = my_chain.inverse_kinematics(target_frame).tolist()
print(str(pos1))

