"""
Program: na01X.py
Programmer: Brian Anders
Date: February 7, 2012

The purpose of this program is to calculate the Fibonacci senquence based on user's input and calculate their successive ratios.
"""


def main():
    """this is the function that runs the main routine, calling all other methods to calculate and print the results"""
    line = raw_input()
    while line != "":
        line = line.strip().split()
        line = [eval(n) for n in line]
        flist = Fib(line[0], line[1], line[2])
                
        printSequence(flist)
        
        line = raw_input()

def Fib(a, b, n):
    """return a Fibonacci senquence list of n length starting with a and b."""
    alist = [a, b]
    for i in range(n-2):
        alist.append(alist[-2] + alist[-1])
    return alist
    
def printSequence(flist):
    """Print two columns of flist with values of n, the fibonacci number at n, and the calculated ratios"""
    print "The first", len(flist), "numbers and their successive ratios"
    print "%5s %15s %10s \t%5s %25s %10s" %("n", "F(n)", "F(n)/F(n-1)", "n", "F(n)", "F(n)/F(n-1)")
    if(len(flist) % 2 == 1): ##odd
        print "%5i %15i \t\t\t%5i %25i %10f" %(1, flist[0], (len(flist)/2) + 2, flist[len(flist)/2 + 1], float(flist[len(flist)/2 + 1])/flist[len(flist)/2])
        for i in range(1, len(flist)/2):
            print "%5i %15i %10f \t%5i %25i %10f" %(i+1, flist[i], float(flist[i])/flist[i-1], i+(len(flist)/2) + 2, flist[i+(len(flist)/2) + 1], float(flist[i+(len(flist)/2) + 1])/flist[i+(len(flist)/2)])
        print "%5i %15i %10f" %((len(flist)/2) + 1, flist[(len(flist)/2)], float(flist[(len(flist)/2)])/flist[(len(flist)/2) - 1])
    else: ##even
        print "%5i %15i \t\t\t%5i %25i %10f" %(1, flist[0], (len(flist)/2) + 1, flist[len(flist)/2], float(flist[len(flist)/2])/flist[len(flist)/2 - 1])
        for i in range(1, len(flist)/2):
            print "%5i %15i %10f \t%5i %25i %10f" %(i+1, flist[i], float(flist[i])/flist[i-1], i+(len(flist)/2) + 1, flist[i + (len(flist) / 2)], float(flist[i + (len(flist) / 2)])/flist[i + (len(flist)/2) - 1])
            


	
main()
