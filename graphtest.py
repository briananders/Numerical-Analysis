from visual.graph import *
from numpy import *

f = gcurve(color = color.cyan)
for x in arange(0., 8.1, 0.1):
    f.plot(pos = (x, 5.*cos(2.*x)))

f1 = gcurve()
x = arange(0., 8.1, 0.01)
y = 5.0* sin(10*x)*cos(2*x)
points = zip(x,y)
##points = [(x[i], y[i]) for i in range(len(x))]
for point in points:
    f1.plot(pos = point, color = color.yellow)


d = gdots(pos = points, color = color.green)
raw_input('Press Enter when ready! ') #Pause to appreciate.
for point in points:
    d.plot(pos = point, color = color.blue)

graph1 = gdisplay(x=0, y=400, width=600, height=150, \
        title='Graph Windown Demo', xtitle='x values', \
        ytitle = 'y values', xmin = -1.0, xmax = 9.0, \
        ymin = -5.0, ymax = 5.0, foreground = color.black, \
        background = color.white)
