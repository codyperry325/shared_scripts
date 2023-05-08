import numpy as np
from numpy import pi
import glob
import os.path
import sys
import ntpath
#from qe_extra import *
import linecache
import pandas as pd

rot_180 = np.array([-1,0,0,0,-1,0,0,0,1]).reshape([3,3])
#print(rot_x)

rot_90 = np.array([1,0,0,0,-1,0,0,0,-1]).reshape([3,3])

atoms = pd.read_fwf("test.xyz", sep=" ")
#print(atoms)

R=np.transpose(atoms)

rot_1=np.dot(rot_180,R)
rot_2=np.dot(rot_90,rot_1)
frac = np.transpose(rot_2)

print(frac)
