# -*- coding: cp1252 -*-
"""
Input matrices and vectors from a file, and outputs augmented matrices.
Brian Anders
2/18/12
"""
from matIO import *
from TriDiagonal import *
from numpy import *



def main():

    linea = []

    f = open('na05in.txt', 'r')
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

        a, b, linea = getMat(linea)     ##reads matrix from file
        
        c,d,e = getCDE(a)       ##gets tri-diagonal into 3 1d arrays

        if i == 0:
            print "\n=========================== Problem 4 ===========================\n"
        else:
            print "\n=========================== Problem 9 ===========================\n"
        printMatA(a, "[A] =")
        print ""
        printMatB(e, " e =")
        print ""
        printMatB(d, " d =")
        print ""
        printMatB(c, " c =")
        print ""
        printMatB(b, " b =")
        print ""

        x = b.copy()

        LUdecomp3(c,d,e)
        printMatB(e, " e =")
        print ""
        printMatB(d, " d =")
        print ""
        printMatB(c, " c =")
        print ""

        LUsolve3(c,d,e,x)
        print ""
        printMatB(x, " x =")
        print ""

        printMatB(dot(a,x)-b, "Ax - b =")
        
    

def getCDE(a):
    c = []
    d = []
    e = []


    for i in range(len(a)-1):
        c.append(a[i+1,i])     ##sub diagonal
        d.append(a[i,i])       ##main diagonal
        e.append(a[i,i+1])     ##super diagonal


    d.append(a[len(a)-1][len(a)-1]) ##last one in main diagonal
    
    return array(c), array(d), array(e)


main()
