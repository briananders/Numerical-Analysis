from numpy import *
from cubicSpline import *
from math import *
from visual.graph import *

def main():

    f = file('na08.txt', 'r')
    points = []
    while True:
        a = f.readline().strip().split()
        
        if(a == []):
##            print "break"
            break
        points += [[int(a[0]),int(a[1])]]
    xData = []
    yData = []
    for point in points:
        xData.append(point[0])
        yData.append(point[1])

    xData = array(xData, dtype=float)
    yData = array(yData, dtype=float)
    cData = arange(len(xData))

    kx = curvatures(cData, xData)
    ky = curvatures(cData, yData)

    d = gdots(pos = points, color = color.green)

    f2 = gcurve(color = color.red)
    
    for x in linspace(0,len(xData),1000):
        f2.plot(pos = (evalSpline(cData, xData, kx, x),evalSpline(cData, yData, ky, x)))

main()
