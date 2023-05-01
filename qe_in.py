import numpy as np
from numpy import pi
import glob
import os.path
import sys
import ntpath
from qe_extra import *

dir = os.getcwd()
files = glob.glob(os.path.join(dir, "*.cif"))

for file in files:
    split = os.path.splitext(file)
    file_name = (split[0]+ '.in')
    with open(file, 'r+') as f, open(file_name,'w+') as i:
        global lattice
        lattice = grab_variables(file)
        printheader(i)   
        for line in f:
               count = 1
               cooot = line.split()
               if len(cooot) == 4:
                    for line in f:
                         count += 1  
               elif len(cooot) == 5:
                    for line in f:
                         count += 1      
        i.write("  nat = " + str(count) + '\n')
        i.write("  a = " + str(lattice[0]) + '\n') 
        i.write("  b = " + str(lattice[1])+ '\n')
        i.write("  c = " + str(lattice[2])+ '\n')
        i.write("  cosBC = " + str(lattice[3])+ '\n')
        i.write("  cosAC = " + str(lattice[4])+ '\n')
        i.write("  cosAB = " + str(lattice[5]))
        print_second(i)
        f.close()
        i.close()
        XVX = int(20/lattice[0])
        YVY = int(20/lattice[1])
        ZVZ = int(20/lattice[2])
        if ZVZ == 0:
               ZVZ = 1
        if XVX == 0:
               XVX = 1
        if YVY == 0:
               YVY = 1
        with open(file, 'r+') as f, open(file_name,'a+') as i:
          i.write(str(XVX) + ' ' + str(YVY) + ' ' +  str(ZVZ) + " 1" + " 1" + " 1" + "\n")
          i.write("\n")
          i.write("ATOMIC_POSITIONS crystal" + "\n")
          for line in f:
               line_s = line.split()
               if len(line_s) == 4:
                    i.write(line)
               elif len(line_s) == 5:
                    line = line[1:]
                    i.write(line)

        

