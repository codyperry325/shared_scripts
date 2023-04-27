import numpy as np
from numpy import pi
import glob
import os.path
import sys

#dir = sys.argv[1]
#files = glob.glob(os.path.join(dir, "*.cif"))

def lines_that_contain(string, fp):
    return [line for line in fp if string in line]

def findvalue(name):
    with open("hello","r") as f:
        for line in lines_that_contain(name,f):
            line = line.split()
            final = line[1]
            return final

def generate_vectors():
    a = float(findvalue("_cell_length_a"))
    b = float(findvalue("_cell_length_b")) 
    c = float(findvalue("_cell_length_c"))
    alpha = float(findvalue("_cell_angle_alpha"))
    beta = float(findvalue("_cell_angle_beta"))
    gamma = float(findvalue("_cell_angle_gamma"))

    cbe = np.cos(beta*pi/180)
    cal = np.cos(alpha*pi/180)
    cga = np.cos(gamma*pi/180) 
    sga = np.sin(gamma*pi/180)
    sbe = np.sin(beta*pi/180)

    N = (cbe - cga*cbe)/sbe

    r21 = b * np.cos(gamma*pi/180)
    r22 = b * np.sin(gamma*pi/180)
    r31 = c * np.cos(beta*pi/180)
    r32 = c * N
    r33 = c * np.sqrt(sbe*sbe-N*N)


    if (alpha == 90 and beta == 90 and gamma == 90):
        v1 = ([a,0,0])
        v2 = ([0,b,0])
        v3 = ([0,0,c])
    else:
        v1 = ([a,0,0])
        v2 = ([r21,r22,0])
        v3 = ([r31,r32,r33])

    final_vector = np.concatenate([v1,v2,v3]).reshape([3,3])
    return final_vector

final = generate_vectors()
print(final)
