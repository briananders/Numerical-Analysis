"""
gaussElimin.py
Brian Anders
2/25/12

Program finds the Gaussian Elimination of Ax=b
"""

from numpy import *
from matIO import *


def gaussElimin(a, b):
    """finds the values of ax = b. a=array b=array, returns arrays a and b."""
    n = len(b)

    for k in range(n-1):        ##makes the lower diagonal = 0.0
        for i in range(k+1, n):
            if a[i, k] != 0.0:
                lam = a[i, k]/a[k, k]
                a[i, k] = 0.0
                a[i, k+1:] = a[i, k+1:] - lam * a[k, k+1:]
                b[i] = b[i] - lam * b[k]

##    printAugMat(a,b)
##    print ""

    for k in range(n-1, -1, -1):    ##makes the main diagonal = 1.0
        if a[k,k] != 0.0:
            lam = a[k,k]
            a[k,k:] = a[k, k:] / lam
            b[k] = b[k] / lam
    
##    printAugMat(a,b)
##    print ""

    for k in range(n-1,-1,-1):      ## substitutes up the columns from the known answers. 1x = y
        lam = b[k]
        for i in range(k-1,-1,-1):
##            print "b[%d] -= a[%d,%d] * %f" %(i, i, k, lam)
            b[i] -= a[i,k] * lam
            a[i,k] = 0.0

##    printAugMat(a,b)
##    print ""

    return a, b



