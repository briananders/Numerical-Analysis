## module LUpivot
''' a,seq = LUdecomp(a,tol=1.0e-9).
    LU decomposition of matrix [a] using scaled row pivoting.
    The returned matrix [a] = [L\U] contains [U] in the upper
    triangle and the nondiagonal terms of [L] in the lower triangle.
    Note that [L][U] is a row-wise permutation of the original [a];
    the permutations are recorded in the vector {seq}.

    x = LUsolve(a,b,seq).
    Solves [L][U]{x} = {b}, where the matrix [a] = [L\U] and the
    permutation vector {seq} are returned from LUdecomp.
'''
from numpy import *
import swap
import error
from matIO import *

def LUpivot(a1, b1, tol=1.0e-9, modifyOriginal=True):
##def LUpivot(a1, modifyOriginal=True):
    if modifyOriginal:
        a = a1
    else:
        a = a1.copy()
        
    n = len(a)
    seq = array(range(n))
    
  # Set up scale factors
    s = zeros(n)
    for i in range(n):
        s[i] = max(abs(a[i,:]))        
    
    for k in range(0,n-1):
        
      # Row interchange, if needed
        p = argmax(abs(a[k:n,k])/s[k:n]) + k
        if abs(a[p,k]) < tol: error.err('Matrix is singular')
        if p != k:
            swap.swapRows(s,k,p)
            swap.swapRows(a,k,p)
            swap.swapRows(seq,k,p)
            
      # Elimination            
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                a[i,k] = lam
                
    b = b1.copy()
    for i in range(n):
        b[i] = b1[seq[i]]
    return a,b,seq

def LUpivotSolve(a,b,seq, tol=1.0e-9):
    n = len(b)
    for k in range(1,n):        ##Forward
        b[k] -= float(dot(a[k,0:k], b[0:k]))
    
    for k in range(n-1,-1,-1):  ##Backward
        if abs(a[k,k]) < tol: error.err('Matrix is singular')
        b[k] = float(b[k] - dot(a[k,k+1:n], b[k+1:n]))/a[k,k]
        
    return b

