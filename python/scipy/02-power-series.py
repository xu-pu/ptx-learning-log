#!/usr/bin/env python

import numpy, math, os
from matplotlib import pyplot
from scipy import optimize, special

PLOT_PATH = os.environ['HOME'] + '/Persistent/scipy-learning'

def get_term(n):
    if n % 2 == 1:
        return lambda x: (-1)**((n-1)/2) * (x**n) / math.factorial(n)
    else: 
        return lambda x: 0

def get_series(depth):
    return lambda x: sum([(get_term(n))(x) for n in range(1, depth+1)])

def power_sin(level):
    pyplot.figure()
    interval = numpy.arange(0.0, 20.0, 0.01)
    for depth in range(1,level+1,2):
        func = get_series(depth)
        pyplot.plot(interval, func(interval), color=(1-depth/level,1-depth/level,0.2))
    pyplot.axis([0,20,-2,2])
    pyplot.title('Power series of sin')
    pyplot.text(1, 1.5, 'iterate depth = %d' % level)
    pyplot.savefig( PLOT_PATH + '/power-sin-'+ str(level) + '.png', dpi=256 )


if __name__ == '__main__':
    for iter_depth in [5,10,20,30,40,50,100]:
        power_sin(iter_depth)
