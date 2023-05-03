import numpy as np
from numpy import pi
import glob
import os.path
import sys
import ntpath
from qe_extra import *
import linecache

dir = os.getcwd()
files = glob.glob(os.path.join(dir, "*.out"))

def line_num(string):
    bound = string
    with open(file, 'r+') as f:
        for num, line in enumerate(f,1):
               if bound in line:
                    return(num)

for file in files:
     with open(file, 'r+') as f:
          begin = line_num("Begin final coordinates")
          end = line_num("End final coordinates")
          for i in range(begin,end):
               with open('test.txt', 'a+') as test:
                    data = linecache.getline(file, i)
                    test.write(data)
                    print(data[0])