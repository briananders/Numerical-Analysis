# -*- coding: cp1252 -*-
"""
Input matrices and vectors from a file, and outputs augmented matrices.
Brian Anders
2/18/12
"""
from matIO import *
from gaussElimin import *
from numpy import *

linea = []

f = open('na03in.txt', 'r')
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
    print "Problem #%d" %(i+10)
    print ""
    a, b, linea = getMat(linea)     ##reads matrices from file
    
    printAugMat(a,b)        ##prints original augmented matrix

    print ""
    
    a, b = gaussElimin(a, b)        ##does the gaussian elimination

##    print "Ax = b implies x = %s T." %str(b)
##    print ""
##
##    print "Ax – b = %s T." %str(a)

    printAugMat(a,b)        ##prints solved augmented matrix
    print ""


    


