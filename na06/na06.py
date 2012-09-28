"""
na06.py
Brian Anders
4/2/12
"""

from matIO import *
from LUpivot import *
from numpy import *
from LUdecomp import *


def main():

    linea = []

    f = open('na06in.txt', 'r')
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

    a, b, linea = getMat(linea)     ##reads matrix from file

    ##Problem 6
    print "========================Problem 6, page 73========================\n"

    doit(a,b)
    
    

    for i in range(2,5):
        print "========================Problem 19, n = ", i, ", page 78========================\n"
        a, b = prob19(i)
##        a, b, linea = getMat(linea)     ##reads matrix from file

        doit(a,b)
        
    
    

def prob19(n):
    a = []
    b = []

    for i in range(n):
        c = []
        for j in range(n):
            c.append(float((i+j)**2))
        a.append(c)
        b.append(sum(c))
    return array(a), array(b)

def doit(a,b):
    printAugMat(a,b, "[A|b] = ", "")
    print ""

    print "Scaled partial pivoting yields:"
    print ""
    x = b.copy()
    a1 = a.copy()
    a1, x, seq = LUpivot(a1,x)
    print seq
    printAugMat(a1, x, "pivoted [A|x] = ","")
    print ""
    x = LUpivotSolve(a1, x, seq)

    printMatB(x, " x = ", "")
    print ""

    printMatB(dot(a,x), " Ax  = ", "")  ##prints the solution
    print ""
    
    print "Check: max|Ax-b| = ", max(abs(dot(a,x)-b))
    print ""

    print "Without pivoting we get:"
    print ""

    LUa = a.copy()      ##to preserve a
    x = b.copy()        ##to preserve b
    
    LUdecomp(LUa)        ##does the Lower Upper Decomposition
    LUsolve(LUa,x)    ##Solves the equation

    printMatB(x, " x  = ", "")  ##prints the solution
    print ""

    printMatB(dot(a,x), " Ax  = ", "")  ##prints the solution
    print ""

    print "Check: max|Ax-b| = ", max(abs(dot(a,x)-b))
    print ""

main()

