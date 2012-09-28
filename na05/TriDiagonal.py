from numpy import *

def LUdecomp3(c,d,e):
    """Doolittle's Decomp of a TriDiagonal system. [c,d,e] where D = main diagonal, C = Subdiagonal, E = Super Diagonal."""
    n = len(d)
    for k in range(0,n-1):
        if(c[k] != 0.0):
            lam = c[k]/d[k]
            c[k] = lam
            d[k+1] -= lam * e[k]
   

def LUsolve3(c,d,e,b):
    """c,d,e must have been through LUdecomp3(c,d,e) first."""
    n = len(d)
    for k in range(1,n):        ##Row 0 changes nothing
        b[k] -= c[k-1] * b[k-1] ## Forward substitution. c = lamda, d = 1, e = 0
    b[n-1] = b[n-1]/d[n-1]
    for k in range(n-2, -1, -1):
        b[k] = (b[k] - e[k] * b[k+1]) / d[k]
    
