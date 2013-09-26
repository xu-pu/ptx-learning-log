#!/usr/bin/env python
#=========================================================================================
# matplotlib tutorial #1 -- simple plotting
# tutorial link -- http://wiki.scipy.org/Cookbook/Matplotlib/SigmoidalFunctions
#=========================================================================================

from matplotlib.mlab import normpdf
import numpy as nx
import pylab as p

#=========================================================================================

def draw_normalpdf():
    x = nx.arange(-4, 4, 0.01) # range with interval
    y = normpdf(x, 0, 1) # Normal PDF -- normal probablility distribution function
    p.plot(x, y, color='red', lw=2)
    p.show()

#=========================================================================================

def boltzman(x, xmid, tau):
    return 1. / (1. + nx.exp(-(x-xmid)/tau))

def draw_boltzman():
    x = nx.arange(-6, 6, 0.01)
    S = boltzman(x, 0, 1)
    Z = 1 - boltzman(x, 0.5, 1)
    p.plot(x, S, x, Z, color='red', lw=2)
    p.show()

#=========================================================================================

def fill_below(x, S, Z):
    ind = nx.nonzero(nx.absolute(S-Z)==min(nx.absolute(S-Z)))[0]
    Y = nx.zeros(S.shape)
    Y[:ind] = S[:ind]
    Y[ind:] = Z[ind:]
    p.fill(x, Y, facecolor='blue', alpha=0.5)

def draw_boltzman_filled():
    x = nx.arange(-6, 6, 0.01)
    S = boltzman(x, 0, 1)
    Z = 1 - boltzman(x, 0.5, 1)
    p.plot(x, S, x, Z, color='red', lw=2)
    fill_below(x, S, Z)
    p.show()
    
#=========================================================================================

if __name__ == '__main__':
    draw_normalpdf()
    draw_boltzman()
    draw_boltzman_filled()

