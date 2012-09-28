from numpy import *

"""
Input matrices and vectors from a file, and outputs augmented matrices.
Brian Anders
2/18/12
"""

def getMat(linea):
    """
    gets full array and returns an array of the appropriate size list (or a matrix)
    """
    
    a = []
    b = []

    while linea[0] == '':       ##clears empty lines
        linea = linea[1:]  

    while linea[0] != '':       ##fill a
        a.append(linea[0].split())
        linea = linea[1:]

    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = float(a[i][j])    ##converts list of strings to list of floats

    while linea[0] == '':       ##clears empty lines
        linea = linea[1:]

    while linea[0] != '' and len(linea) != 0:       ##fill b
        b.append(linea[0].split())
        linea = linea[1:]

    for i in range(len(b)):
        for j in range(len(b[i])):
            b[i][j] = float(b[i][j])    ##converts list of strings to list of floats

    newb = []
    for i in range(len(b)):
        for j in range(len(b[i])):
            newb.append(b[i][j])        ##makes b 1d.

    a = array(a)
    b = array(newb)

    return a, b, linea

def printAugMat(a,b):
    """
    prints two 2d arrays a and b as the augmented matrix [a|b]
    """
    stringa = []
    for i in range(len(a)): #builds every string to be printed and puts it in an array
        string = ""
        string += "[ "
        for j in range(len(a[0])):
            string += str(("%5.2f" % a[i][j])) + " " #%5.2f = float number with a total lenght of 5 (counting the decimal) with 2 decimal places.
        string += "| "
        string += str(("%5.2f" % b[i])) #%5.2f = float number with a total lenght of 5 (counting the decimal) with 2 decimal places.
        string += " ]"
        stringa.append(string)
    for i in range(len(stringa)): #prints the string array
        if(len(stringa) % 2 == 0): #even sized matrix
            if(len(stringa) / 2 == i+1):
                print "[A|b] =", stringa[i]
            else:
                print "\t", stringa[i]

        else:   #odd sized matrix
            if(len(stringa) / 2 == i):
                print "[A|b] =", stringa[i]
            else:
                print "\t", stringa[i]
