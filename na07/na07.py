from newtonPoly import *
from numpy import *
from math import *
from visual.graph import *

def main():

    a = raw_input("a,b = ")

    a = a.replace(","," ")
    a = a.strip().split()

    b = int(a[1])
    a = int(a[0])

##    if(a < 2):
##        a = 2
##    if(b < 2):
##        b = 2
##    if(a >= 32):
##        a = 32
##    if(b >= 32):
##        b = 32
    
    if(b < a):
        temp = a
        a = b
        b = temp

    maxerror = 0.0
    minerror = 100.0
    maxi = 0
    mini = 0

    errx = range(a,b)
    erry = []

    print "\nn\tError"

    for i in range(a,b):
        
        pi, pm = plotter(i)
        gdisplay()

        erry.append(pm)
        print "%d\t%4.1e" %(pi, pm)
                    
        if(maxerror < pm):
            maxerror = pm
            maxi = pi

        if(minerror > pm):
            minerror = pm
            mini = pi

    
    gdisplay(title="Error Plot")
    points = zip(errx,erry)
    gdots(pos = points, color = color.green) 

    print ""
    print "%d\t%.5f <-- maximum error" %(maxi, maxerror)
    print "%d\t%.5f <-- minimum error" %(mini, minerror)
    
def data(n):
    x = linspace(-3,3,n)
    y = f(x)
    return x, y
        

def f(x):
    return 3.0/(1 + x**2)

def plotter(i):
    ss = "i = "
    ss += str(i)
    gdisplay(title=ss)
    xData, yData = data(i)

    interp = coeffts(xData, yData)

    f1 = gcurve()
    x = linspace(-3,3,201)
    y = f(x)
    points = zip(x,y)
    for point in points:
        f1.plot(pos = point, color = color.red)

    x = linspace(-3,3,i)
    y = f(x)
    points = zip(x,y)

    d = gdots(pos = points, color = color.green)

    f2 = gcurve()
    x = linspace(-3,3,201)
    y = evalPoly(interp,xData,x)
    points = zip(x,y)
    for point in points:
        f2.plot(pos = point, color = color.blue)

    return i, max([abs(evalPoly(interp, xData, n) - f(n)) for n in linspace(-3,3,201)])

main()
