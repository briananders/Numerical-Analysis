"""
Input matrices and vectors from a file, and outputs augmented matrices.
Brian Anders
2/18/12
"""

def getMat(linearray):
    """
    gets full array and returns an array of the appropriate size list (or a matrix)
    """
##    print linearray[0]
    size = len(linearray[0]) #determines what euclidian space the matrix occupies
    a = []
    for i in range(size):
        a.append(linearray[0])
        linearray = linearray[1:]## drops off the data as it is used.
    b = linearray[0]
    linearray = linearray[1:]
    while (len(b) < len(a)): #makes sure that b has the right amount of numbers to match the matrix
        b += linearray[0]
        linearray = linearray[1:]## drops off the data as it is used.
    
    return a, b, linearray #returns A, b and the changed input array.

def printAugMat(a,b):
    """
    prints two 2d arrays a and b as the augmented matrix [a|b]
    """
    stringa = []
    for i in range(len(a[0])): #builds every string to be printed and puts it in an array
        string = ""
        string += "[ "
        for j in range(len(a[0])):
            string += str(("%5.2f" % eval(a[i][j]))) + " " #%5.2f = float number with a total lenght of 5 (counting the decimal) with 2 decimal places.
        string += "| "
        string += str(("%5.2f" % eval(b[i]))) #%5.2f = float number with a total lenght of 5 (counting the decimal) with 2 decimal places.
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
