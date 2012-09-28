from numpy import *
from matIO import *

def LUdecomp(a):
   """Doolittle's decompositon of A into [L\U], Lii = 1"""
   n = len(a)
   for k in range(n-1):
       for i in range (k+1, n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                a[i,k] = lam

def LUsolve(a,b):
    """Solve Ax = b where [A] = [L\U]"""
    n = len(b)
    for k in range(1,n):        ##Forward
        b[k] -= dot(a[k,0:k], b[0:k])
    for k in range(n-1,-1,-1):  ##Backward
        b[k] = (b[k] - dot(a[k,k+1:n], b[k+1:n]))/a[k,k]
   

def Hilbert(n):
   """Returns a Hilbert matrix of size nxn, where b = <1,1,1,...,1>"""
   h = [1.0/(i) for i in range( 1, 2*n)]
   b = [1.0 for i in range(n)]
   return array([h[j : j + n] for j in range(n)]), array(b)


def interpolate(x):
   """takes array of sets, returns polynomial"""
   n = len(x)     ##to determine
##   n = len(x[0]) ##to determine size. i.e. a0, a1, a2...,an

   a = []
   b = []
   for i in range(n):
      b.append(x[i,1])
      row = [1.0]
      for j in range(n-1):
         row.append(x[i,0]**(j+1))
      a.append(row)
   return array(a), array(b)
         
   


   

   
   

   
