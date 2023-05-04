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
     split = os.path.splitext(file)
     file_name = (split[0]+ '.cif')
     latt_name = (split[0] + '.txt')
     atom_name = (split[0] + '.atoms')
     with open(file, 'r+') as f:
          begin = line_num("Begin final coordinates")
          end = line_num("End final coordinates")
          begin2 = line_num("crystal axes: (cart. coord. in units of alat)")
          end2 = (int(begin2) + 4)
          word = "lattice parameter"
          read = f.readlines()
          for line in read:
               if word in line:
                    alat = line_num(line)
                    #print(alat)
                    alatout = float(linecache.getline(file,alat).split()[4])
                    #print(alatout)
          for i in range(begin2,end2):
               latticenumbers = linecache.getline(file,i)
               #print(latticenumbers)
               with open(latt_name, 'a+') as la:
                    la.write(latticenumbers)


with open("QQQFDJ01newnewnewnew.txt","r+") as hello:
     alat = float(alatout)
     a1 = np.array(linecache.getline("QQQFDJ01newnewnewnew.txt",2).split()[3])
     a2 = np.array(linecache.getline("QQQFDJ01newnewnewnew.txt",2).split()[4])
     a3 = np.array(linecache.getline("QQQFDJ01newnewnewnew.txt",2).split()[5])
     a = np.array([a1,a2,a3],dtype=float)
     b1 = np.array(linecache.getline("QQQFDJ01newnewnewnew.txt",3).split()[3])
     b2 = np.array(linecache.getline("QQQFDJ01newnewnewnew.txt",3).split()[4])
     b3 = np.array(linecache.getline("QQQFDJ01newnewnewnew.txt",3).split()[5])
     b = np.array([b1,b2,b3],dtype=float)
     c1 = np.array(linecache.getline("QQQFDJ01newnewnewnew.txt",4).split()[3])
     c2 = np.array(linecache.getline("QQQFDJ01newnewnewnew.txt",4).split()[4])
     c3 = np.array(linecache.getline("QQQFDJ01newnewnewnew.txt",4).split()[5])
     c = np.array([c1,c2,c3],dtype=float)
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
     print(alat,Adone,Bdone,Cdone,gamma,alpha,beta)