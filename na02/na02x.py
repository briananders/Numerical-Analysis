"""
Input matrices and vectors from a file, and outputs augmented matrices.
Brian Anders
2/18/12
"""
from matIO import *
from numpy import *


linearray = []

f = open('na02in.txt', 'r')
for line in f:
    linearray.append(line.strip().split())
f.close()

for i in linearray:
    for j in range(len(i)):
        if(i[j][0] == "#"):
            for k in range(len(i)-j):
                i.pop() # removes all the commented out lines
            break
        
linearray = filter (lambda a: a != [], linearray) #removes blank lines

##print linearray[0]
itera = eval(linearray[0][0])  ##determines how many matrices there are
linearray = linearray[1:] ## drops off the data as it is used.

for count in range(itera):
    a, b, linearray = getMat(linearray)
    printAugMat(a, b)
    print ""
    


