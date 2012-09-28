from numpy import *

"""
Input matrices and vectors from a file, and outputs augmented matrices.
Brian Anders
2/18/12
"""

def getMat(linea):
    """
    Gets full array and returns an array of the appropriate size list (or a matrix)
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



def printAugMat(a,b, pref, post):
    """
    prints 2D array a and 1D array b as the augmented matrix [a|b] with a preface (i.e. "[A|b] =") and a postface (i.e. "T")
    """
    stringa = []
    prefs = ""
    for i in range(len(pref)):
        prefs += " "
    for i in range(len(a)): #builds every string to be printed and puts it in an array
        string = ""
        string += "[ "
        for j in range(len(a[0])):
            string += str(("%7.2f" % a[i][j])) + " " #%6.2f = float number with a total length of 6 (counting the decimal) with 2 decimal places.
        string += "| "
        string += str(("%7.2f" % b[i])) #%6.2f = float number with a total lenght of 6 (counting the decimal) with 2 decimal places.
        string += " ]"
        stringa.append(string)
    for i in range(len(stringa)): #prints the string array
        if(len(stringa) % 2 == 0): #even sized matrix
            if(len(stringa) / 2 == i+1):
                print pref, stringa[i], post
            else:
                print prefs, stringa[i]

        else:   #odd sized matrix
            if(len(stringa) / 2 == i):
                print pref, stringa[i], post
            else:
                print prefs, stringa[i]



def printAugMatH(a,b, pref, post):
    """
    prints 2D array a and 1D array b as the augmented matrix [a|b] with a preface (i.e. "[A|b] =") and a postface (i.e. "T")
    intended for Hilbert matrix where numbers will be 0.0... to save room on the left side of the decimal.
    """
    stringa = []
    prefs = ""
    for i in range(len(pref)):
        prefs += " "
    for i in range(len(a)): #builds every string to be printed and puts it in an array
        string = ""
        string += "[ "
        for j in range(len(a[0])):
            string += str(("%.6f" % a[i][j])) + " " 
        string += "| "
        string += str(("%.6f" % b[i])) 
        string += " ]"
        stringa.append(string)
    for i in range(len(stringa)): #prints the string array
        if(len(stringa) % 2 == 0): #even sized matrix
            if(len(stringa) / 2 == i+1):
                print pref, stringa[i], post
            else:
                print prefs, stringa[i]

        else:   #odd sized matrix
            if(len(stringa) / 2 == i):
                print pref, stringa[i], post
            else:
                print prefs, stringa[i]


def printMatA(a, pref, post):
    """
    prints 2D array a as the matrix [a] with a preface (i.e. "[A|b] =") and a postface (i.e. "T")
    """
    stringa = []
    prefs = ""
    for i in range(len(pref)):
        prefs += " "
    for i in range(len(a)): #builds every string to be printed and puts it in an array
        string = ""
        string += "[ "
        for j in range(len(a[0])):
            string += str(("%7.2f" % a[i][j])) + " " #%6.2f = float number with a total length of 6 (counting the decimal) with 2 decimal places.
        string += "]"
        stringa.append(string)
    for i in range(len(stringa)): #prints the string array
        if(len(stringa) % 2 == 0): #even sized matrix
            if(len(stringa) / 2 == i+1):
                print pref, stringa[i]
            else:
                print prefs, stringa[i], post

        else:   #odd sized matrix
            if(len(stringa) / 2 == i):
                print pref, stringa[i], post
            else:
                print prefs, stringa[i]



def printMatB(a, pref, post):
    """
    prints 2D array a with a preface (i.e. "[A|b] =") and a postface (i.e. "T")
    """
    stringa = []
    prefs = ""
    for i in range(len(pref)):
        prefs += " "
    for i in range(len(a)): #builds every string to be printed and puts it in an array
        string = str(("[ %15.6f ]" % a[i]))
        stringa.append(string)
    for i in range(len(stringa)): #prints the string array
        if(len(stringa) % 2 == 0): #even sized matrix
            if(len(stringa) / 2 == i+1):
                print pref, stringa[i], post
            else:
                print prefs, stringa[i]

        else:   #odd sized matrix
            if(len(stringa) / 2 == i):
                print pref, stringa[i], post
            else:
                print prefs, stringa[i]

def printMatB_raw(a, pref, post):
    """
    prints 2D array a in the raw form 1e-14 with a preface (i.e. "[A|b] =") and a postface (i.e. "T")
    """
    stringa = []
    prefs = ""
    for i in range(len(pref)):
        prefs += " "
    for i in range(len(a)): #builds every string to be printed and puts it in an array
        string = "[" + str(a[i]) + "]"     
        stringa.append(string)
    for i in range(len(stringa)): #prints the string array
        if(len(stringa) % 2 == 0): #even sized matrix
            if(len(stringa) / 2 == i+1):
                print pref, stringa[i], post
            else:
                print prefs, stringa[i]

        else:   #odd sized matrix
            if(len(stringa) / 2 == i):
                print pref, stringa[i], post
            else:
                print prefs, stringa[i]


def printPoly(x):
    """prints a nice polynomial equation from an array(x)"""

    n = len(x) ##size of euclidian space.

    string = "p(x) = "
    for i in range(n):
        if(x[i] != 0.0):
            if(i==0):
                string += str(float(x[i]))
            else:
                if(x[i] < 0):
                    string += " - "
                else:
                    string += " + "
                    
                if(i==1):
                    string += "%.3f*x" %(abs(x[i]))
                else:
                    string += "%.3f*x**%d" %(abs(x[i]),i)
    print string




















    

