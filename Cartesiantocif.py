from cmath import sqrt
import numpy as np
#from numpy import pi
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

########################################################################################################################
     #This part of the code will construct a unit cell box from crystal 17 input files
########################################################################################################################
pie = 3.141592653589793238

a = np.array([AAAA])
b = np.array([BBBB])
c = np.array([CCCC])

ab = np.dot(a,b)
bc = np.dot(b,c)
ac = np.dot(a,c)

A = np.sqrt((np.dot(a,a)))
C = np.sqrt((np.dot(c,c)))
B = np.sqrt((np.dot(b,b)))

gamma = np.arccos((ab)/(A*B))
alpha = np.arccos((bc)/(B*C))
beta = np.arccos((ac)/(A*C))

gammadeg = np.arccos((ab)/(A*B))*(180/pie)
alphadeg = np.arccos((bc)/(B*C))*(180/pie)
betadeg = np.arccos((ac)/(A*C))*(180/pie)

print("alpha =", alphadeg)
print("beta = ", betadeg)
print("gamma =", gammadeg)

Adone = A
Bdone = B
Cdone = C

print("Alen =", Adone)
print("Blen =", Bdone)
print("Clen =", Cdone)

cosBC = np.cos(alpha)
cosAC = np.cos(beta)
cosAB = np.cos(gamma)

print("cosBC =", cosBC)
print("cosAC =", cosAC)
print("cosAB =", cosAB)


########################################################################################################################
     #This part of the code will house the cartesian coordinates
########################################################################################################################

vcartesian = pd.read_fwf("XXX.txt", sep="   ")


########################################################################################################################
     #This part of the code will construct fractional coordinates from the box that is created above.
########################################################################################################################

#creation of variables for the 3x3 matrix

omega = A*B*C*sqrt(1-cosBC*cosBC-cosAC*cosAC-cosAB*cosAB+2*(cosAB*cosBC*cosAC))

#print(omega)

r=np.zeros((3,3))

r[0,0] = 1/A
r[0,1] = -(cosAB)/(A*np.sin(gamma))
r[0,2] = B*C*(cosBC*cosAB-cosAC)/(omega*np.sin(gamma))

r[1,0] = 0
r[1,1] = 1/(B*np.sin(gamma))
r[1,2] = A*C*(cosAC*cosAB-cosBC)/(omega*np.sin(gamma))

r[2,0] = 0
r[2,1] = 0
r[2,2] = A*B*(np.sin(gamma))/omega 

#print(r)
R=np.transpose(vcartesian)

v_set = np.dot(r,R)
vfractional = np.transpose(v_set)
print(vfractional)