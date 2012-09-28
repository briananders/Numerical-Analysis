# -*- coding: cp1252 -*-
"""
Input matrices and vectors from a file, and outputs augmented matrices.
Brian Anders
2/18/12
"""
from matIO import *
from LUdecomp import *
from numpy import *



def main():

    linea = []

    f = open('na04in.txt', 'r')
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

    prob8(a,b) 

    a, b, linea = getMat(linea)     ##reads matrix from file
    
    prob15() ##no input. just placeholders in the input file

    a, b, linea = getMat(linea)     ##reads matrix from file

    prob18(a,b) ##only needs a.


def prob8(a,b):
    print "================================ Problem 8 ================================\n"
 
    printAugMat(a,b, "[A|b] =", "")        ##prints original augmented matrix

    print ""
    LUa = a.copy()      ##to preserve a
    x = b.copy()        ##to preserve b
    
    LUdecomp(LUa)        ##does the Lower Upper Decomposition
    printMatA(LUa, "[L\U] =", "")    ## Prints the Lower Upper Decomposition

    print ""

    LUsolve(LUa,x)    ##Solves the equation
    printMatB(x, "  x  = ", "T")  ##prints the solution

    print ""

    printMatB(dot(a,x)-b, "Ax-b =", "T")
    print ""
    printMatB_raw(dot(a,x)-b, "Ax-b(raw) =", "T")
    print ""


def prob15():
    print "\n================================ Problem 15 ================================\n"

    n = 5       ##nxn size of hilbert matrix

    print "#####The largest n with solution correct to 6 decimal places is n = %d\n" %n
    print "The system is:"

    a, b = Hilbert(n)
    printAugMatH(a, b, "[A|b] =", "")

    print ""
    
    LUa = a.copy()      ##to preserve a
    x = b.copy()        ##to preserve b
    
    LUdecomp(LUa)        ##does the Lower Upper Decomposition
    ##printMatA(LUa, "[L\U] =")    ## Prints the Lower Upper Decomposition

    LUsolve(LUa,x)    ##Solves the equation
    printMatB(x, "The solution is x =", "T")  ##prints the solution

    print ""
    
    print "The largest error is " + str(max(abs(dot(a,x)-b))) + "\n"

    printMatB(dot(a,x)-b, "Ax-b =", "T")
    print ""
    printMatB_raw(dot(a,x)-b, "Ax-b(raw) =", "T")
    print ""

def prob18(a,b):
    print "\n================================ Problem 18 ================================\n"

    printMatA(a, "[A] =", "")

    print ""
    a,b = interpolate(a)

    LUa = a.copy()      ##to preserve a
    x = b.copy()        ##to preserve b

    printAugMat(a,b, "p(x) = ", "")
    print ""

    LUdecomp(LUa)        ##does the Lower Upper Decomposition
##    printMatA(LUa, "[L\U] =")    ## Prints the Lower Upper Decomposition
    
    LUsolve(LUa,x)    ##Solves the equation

    printMatB(x, " x =", "")  ##prints the solution
    print ""

    printPoly(x)
 
    
    
    

main()
