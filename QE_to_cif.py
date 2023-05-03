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

#def vec(vector):
     #a = 


for file in files:
     split = os.path.splitext(file)
     file_name = (split[0]+ '.cif')
     with open(file, 'r+') as f:
          begin = line_num("Begin final coordinates")
          end = line_num("End final coordinates")
          for i in range(begin,end):
               with open('coords.txt', 'a+') as coords, open('test.txt', 'a+') as test:
                    data = linecache.getline(file, i)
                    if "density" not in data:
                         if "volume" not in data:
                              if "Begin" not in data:
                                   line_s = data.split()
                                   if len(line_s) == 4:
                                        with open(file_name, 'a+') as cif:
                                             atoms = data
                                             #print(atoms)
                                             #cif.write(atoms)
                                   if "CELL" not in data:
                                        new = []
                                        #if len(line_s) == 3:
                                        [for line in data if len(line_s) == 3:]
                                             lattcorr = line_s 
                                             new.append(line_s)
                                             newarray = np.array(new)
                                   if "CELL" in data:
                                        alat = data.split(")")
                                        finalalat = ' '.join(alat).split()
                                        alattotal = finalalat[2]
                                        print(alattotal)

print(newarray)