"""
Input matrices and vectors from a file, and outputs augmented matrices.
Brian Anders
2/18/12
"""
from matIO import *
from numpy import *

linea = []

f = open('na02in.txt', 'r')
for line in f:
    linea.append(line)
f.close()

for s in range(len(linea)):
    newl = ""
    for i in range(len(linea[s])):
        if(linea[s][i] == "#"):
            break
        newl += linea[s][i]
    linea[s] = newl.strip()

linea.append('')

itera = int(linea[0])
linea = linea[1:]

for i in range(itera):
    a,b, linea = getMat(linea)
    printAugMat(a,b)
    print ""


    


