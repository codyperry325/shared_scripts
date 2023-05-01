import numpy as np
from numpy import pi

a = np.array([AAAA])
b = np.array([BBBB])
c = np.array([CCCC])

ab = np.dot(a,b)
bc = np.dot(b,c)
ac = np.dot(a,c)

A = np.sqrt((np.dot(a,a)))

C = np.sqrt((np.dot(c,c)))

B = np.sqrt((np.dot(b,b)))

gamma = np.arccos((ab)/(A*B))*(180/pi)

alpha = np.arccos((bc)/(B*C))*(180/pi)
print("alpha =", alpha)

beta = np.arccos((ac)/(A*C))*(180/pi)
print("beta = ", beta)

print("gamma =", gamma)

alat = (ALA)

Adone = A*alat*0.529177
Bdone = B*alat*0.529177
Cdone = C*alat*0.529177
print("Alen =", Adone)
print("Blen =", Bdone)
print("Clen =", Cdone)

cosBC = np.cos(alpha)
cosAC = np.cos(beta)
cosAB = np.cos(gamma)

print("cosBC =", cosBC)
print("cosAC =", cosAC)
print("cosAB =", cosAB)
