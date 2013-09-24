#!/usr/bin/env python

import os
import numpy
from scipy import special, optimize
from matplotlib import pyplot

PLOT_PATH = os.environ['HOME'] + '/Persistent/scipy-learning'

def hello_world():
    # compute maxium
    f = lambda x: -special.jv(3,x)
    sol  = optimize.minimize(f,1.0)

    # plot
    x = numpy.linspace(0,10,5000)
    pyplot.plot(x, special.jv(3,x), '-', sol.x, -sol.fun, 'o')

    # produce output
    pyplot.savefig( PLOT_PATH + '/hello-world.png', dpi=96 )


def linear_graph():
    pyplot.plot([1,2,3,4],[3,6,7,8],'ro')
    pyplot.plot([1,2,3,4],[3,6,7,8])

    t = numpy.arange(0.0, 5.0, 0.1)
    pyplot.plot(t, t,    'r--', 
                t, t**2, 'bs', 
                t, t**3, 'g^')

    pyplot.axis([0,6,0,10])
    pyplot.savefig( PLOT_PATH + '/linear-graph.png', dpi=96 )

def figure_control():
    f = lambda t: numpy.exp(-t) * numpy.cos(2*numpy.pi*t)
    t1 = numpy.arange(0.0, 5.0, 0.1)
    t2 = numpy.arange(0.0, 5.0, 0.02)

    pyplot.figure(1)
    pyplot.subplot(211)
    pyplot.plot(t1, f(t1), 'bo', 
                t2, f(t2), 'k')
    

    pyplot.subplot(212)
    pyplot.plot(t2, numpy.cos(2*numpy.pi*t2), 'r--')

    pyplot.savefig( PLOT_PATH + '/figure-control.png', dpi=96 )

def figure_text():
    mu, sigma = 100, 15
    x = mu + sigma * numpy.random.randn(10000)
    n, bins, patches = pyplot.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

    pyplot.xlabel('Smarts')
    pyplot.ylabel('Probability')
    pyplot.title('Histogram of IQ')
    pyplot.text(60, 0.025, r'$\mu=100,\ \sigma=15$')
    pyplot.axis([40,160,0,0.03])
    pyplot.grid(True)

    pyplot.savefig( PLOT_PATH + '/figure-text.png', dpi=96 )

def figure_annotate():
    pyplot.subplot(111)
    
    t = numpy.arange(0.0, 5.0, 0.01)
    s = numpy.cos(2*numpy.pi*t)
    pyplot.plot(t,s,lw=2)
    
    pyplot.annotate('local max', xy=(2,1), xytext=(3,1.5),arrowprops=dict(facecolor='black', shrink=0.05))
    
    pyplot.ylim(-2,2)
    pyplot.savefig( PLOT_PATH + '/figure_annotate.png', dpi=96 )

if __name__ == '__main__':
    figure_annotate()
