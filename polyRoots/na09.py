from math import *
from numpy import *
from visual.graph import *

from rootsearch import *
from bisection import *
from newtonRaphson import *
from ridder import *


def f(x):
    return sin(x)

def df(x):
    return cos(x)

def main():
    low = float(raw_input("low = "))
    high = float(raw_input("high = "))
    step = float(raw_input("step = "))

    root = rootsearch(f, low, high, step)
    bisect = bisection(f, low, high)
    newton = newtonRaphson(f, df, low, high)
    ridders = ridder(f, low, high)

    correct = math.pi
    
    print "rootsearch =", root
    print "rootsearch error =", max(abs(correct - root[0]), abs(correct - root[1]))
    print ""
    print "bisection =", bisect
    print "bisection error =", abs(correct - bisect)
    print ""
    print "newtonRaphson =", newton
    print "newton error =", abs(correct - newton)
    print ""
    print "ridder =", ridders
    print "ridder error =", abs(correct - ridders)
    print ""
    print ""
    print "Average root =", (((root[0] + root[1])/2.0) + bisect + newton + ridders)/4.0
    print "Average root error =", abs(((((root[0] + root[1])/2.0) + bisect + newton + ridders)/4.0)-correct)
    print ""
    print "Most Accurate root =", min(min(abs(correct - root[0]), abs(correct - root[1])), abs(correct - bisect), \
                                      abs(correct - newton), abs(correct - ridders))
    print "Least Accurate root =", max(max(abs(correct - root[0]), abs(correct - root[1])), abs(correct - bisect), \
                                      abs(correct - newton), abs(correct - ridders))


    gdisplay(title="Root Search")
    f1 = gcurve()
    for x in linspace(low-1,high+1,200):
        f1.plot(pos = (x,f(x)), color = color.red)
    f2=gdots(pos = [low, f(low)], color = color.yellow)
    gdots(pos = [high, f(high)], color = color.yellow)
    gdots(pos = [(root[0],f(root[0])),(root[1],f(root[1]))], color = color.green)


    gdisplay(title="Bisection")
    f1 = gcurve()
    for x in linspace(low-1,high+1,200):
        f1.plot(pos = (x,f(x)), color = color.red)
    gdots(pos = [low, f(low)], color = color.yellow)
    gdots(pos = [high, f(high)], color = color.yellow)
    gdots(pos = [bisect,0], color = color.green)


    gdisplay(title="Newton Raphson")
    f1 = gcurve()
    for x in linspace(low-1,high+1,200):
        f1.plot(pos = (x,f(x)), color = color.red)
    gdots(pos = [low, f(low)], color = color.yellow)
    gdots(pos = [high, f(high)], color = color.yellow)
    gdots(pos = [newton,0], color = color.green)


    gdisplay(title="Ridder")
    f1 = gcurve()
    for x in linspace(low-1,high+1,200):
        f1.plot(pos = (x,f(x)), color = color.red)
    gdots(pos = [low, f(low)], color = color.yellow)
    gdots(pos = [high, f(high)], color = color.yellow)
    gdots(pos = [ridders,0], color = color.green)

    gdisplay(title="Combination: RootSearch(white), Bisection(yellow), NewtonRaphson(blue), Ridders(green)")
    f1 = gcurve()
    for x in linspace(low-1,high+1,200):
        f1.plot(pos = (x,f(x)), color = color.red)
        
    
    gdots(pos = [low, f(low)], color = color.yellow)
    gdots(pos = [high, f(high)], color = color.yellow)
    gdots(pos = [(root[0],f(root[0])),(root[1],f(root[1]))], color = color.white)
    gdots(pos = [bisect,0], color = color.yellow)
    gdots(pos = [newton,0], color = color.blue)
    gdots(pos = [ridders,0], color = color.green)

        
    

main()
