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

def vec(file,alat,file_name):
     with open(file,"r+"), open(file_name, 'a+') as i:
          alat = float(alat)
          a = (linecache.getline(file,1).split())
          b = (linecache.getline(file,2).split())
          c = (linecache.getline(file,3).split())
          a = np.array(a,dtype=float)
          b = np.array(b,dtype=float)
          c = np.array(c,dtype=float)
          ab = np.dot(a,b)
          bc = np.dot(b,c)
          ac = np.dot(a,c)
          A = np.sqrt((np.dot(a,a)))
          C = np.sqrt((np.dot(c,c)))
          B = np.sqrt((np.dot(b,b)))

          gamma = np.arccos((ab)/(A*B))*(180/pi)
          alpha = np.arccos((bc)/(B*C))*(180/pi)
          beta = np.arccos((ac)/(A*C))*(180/pi)

          Adone = A*alat*0.529177
          Bdone = B*alat*0.529177
          Cdone = C*alat*0.529177

          i.write("_cell_length_a " + str(Adone) + '\n')
          i.write("_cell_length_b " + str(Bdone) + '\n')
          i.write("_cell_length_c " + str(Cdone) + '\n')
          i.write("_cell_angle_alpha " + str(alpha) + '\n')
          i.write("_cell_angle_beta " + str(beta) + '\n')
          i.write("_cell_angle_gamma " + str(gamma) + '\n')
          return Adone, Bdone,Cdone,alpha,beta,gamma

for file in files:
     split = os.path.splitext(file)
     file_name = (split[0]+ '.cif')
     latt_name = (split[0] + '.txt')
     atom_name = (split[0] + '.atoms')
     with open(file, 'r+') as f:
          begin = line_num("Begin final coordinates")
          end = line_num("End final coordinates")
          for i in range(begin,end):
               data = linecache.getline(file, i)
               if "density" not in data:
                    if "volume" not in data:
                          if "Begin" not in data:
                              line_s = data.split()
                              if len(line_s) == 4:
                                   with open(atom_name, 'a+') as cif:
                                        atoms = data
                                        cif.write(atoms)
                              if "CELL" not in data:      
                                   if len(line_s) == 3:
                                        with open(latt_name, 'a+') as la:
                                             lattcorr = str(data)
                                             new = np.array(lattcorr)
                                             la.write(lattcorr)
                              if "CELL" in data:
                                   alat = data.split(")")
                                   finalalat = ' '.join(alat).split()
                                   alattotal = float(finalalat[2])
     with open(file_name, "a+") as i:
          mercury1(i)
          i.close()
     with open(file_name, "a+") as i:
          vec(latt_name,alattotal,file_name)
          i.close()
     with open(file_name, "a+") as i, open(atom_name, 'r+') as atom:
          mercury2(i)
          for line in atom:
               line_s = line.split()
               if len(line_s) == 4:
                    i.write(line)

     if os.path.exists(latt_name):
          os.remove(latt_name)
     if os.path.exists(atom_name):
          os.remove(atom_name)