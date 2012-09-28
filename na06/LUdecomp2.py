## module LUdecomp
''' a = LUdecomp(a).
    LU decomposition: [L][U] = [a]. The returned matrix [a] = [L\U]
    contains [U] in the upper triangle and the nondiagonal terms
    of [L] in the lower triangle.

    x = LUsolve(a,b).
    Solves [L][U]{x} = b, where [a] = [L\U] is the matrix returned
    from LUdecomp.
'''
from numpy import *
from matIO import *

def LUdecomp(a1, tol=1e-9, modifyOriginal=True):
   """Doolittle's decompositon of A into [L\U], Lii = 1"""
   print "LUdecomp()+++++++++++++++++++"
   printMatA(a1,"test = ", "")
   
   if modifyOriginal:
       a = a1
   else:
       a = a1.copy()
   n = len(a)
   for k in range(n-1):
       if(abs(a[k,k]) < tol):
          print "a[k,k] is small", a[k,k]
       for i in range (k+1, n):
            if a[i,k] != 0.0:
                
                try:
                    lam = a[i,k]/a[k,k]
                    print "lam = %f" %lam
                    a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                    a[i,k] = lam
                except ZeroDivisionError:
                    print "divide by zero. you can't do that."
                    

def LUsolve(a,b):
    """Solve Ax = b where [A] = [L\U]"""
    n = len(b)
    for k in range(1,n):        ##Forward
        b[k] -= dot(a[k,0:k], b[0:k])
    for k in range(n-1,-1,-1):  ##Backward
        try:
            b[k] = (b[k] - dot(a[k,k+1:n], b[k+1:n]))/a[k,k]
        except ZeroDivisionError:
            print "divide by zero. you can't do that."
