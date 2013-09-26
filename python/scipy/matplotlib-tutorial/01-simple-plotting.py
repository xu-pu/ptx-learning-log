#!/usr/bin/env python
#=========================================================================================
# matplotlib tutorial #1 -- simple plotting
# tutorial link -- http://wiki.scipy.org/Cookbook/Matplotlib/SigmoidalFunctions
#=========================================================================================

from matplotlib.mlab import normpdf
import matplotlib.numpy as nx
from numpy import sin, cos, exp, pi, arange
from matplotlib.numpy.mlab import mean
import pylab as p

#=========================================================================================

def draw_normalpdf():
    x = arange(-4, 4, 0.01) # range with interval
    y = normpdf(x, 0, 1) # Normal PDF -- normal probablility distribution function
    p.plot(x, y, color='red', lw=2)
    p.show()

#=========================================================================================

def boltzman(x, xmid, tau):
    return 1. / (1. + exp(-(x-xmid)/tau))

def draw_boltzman():
    x = arange(-6, 6, 0.01)
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
    x = arange(-6, 6, 0.01)
    S = boltzman(x, 0, 1)
    Z = 1 - boltzman(x, 0.5, 1)
    p.plot(x, S, x, Z, color='red', lw=2)
    fill_below(x, S, Z)
    p.show()
    
#=========================================================================================

s1 = sin(2*pi*t)
s2 = exp(-t)
s3 = sin(2*pi*t)*exp(-t)
s4 = sin(2*pi*t)*cos(4*pi*t)
s5 = s1*s2
s6 = s1-s4
s7 = s3*s4-s1

def multi_line():
    t = arange(0.0, 2.0, 0.01)
    p.plot(t, s1,
           t, s2+1,
           t, s3+2,
           t, s4+3,
           color='k')
    p.ylim(-1,4)
    p.yticks(arange(4), ['S1','S2','S3','S4'])
    p.show()

def multi_axes():
    t = arange(0.0, 2.0, 0.01)    
    fig = p.figure()
    yprops = dict(rotation=0,
                  horizontalalignment='right',
                  verticalalignment='center',
                  x=-0.01)
    axprops = dict(yticks=[])
    
    ax1 = fig.add_axes([0.1, 0.7, 0.8, 0.2], **axprops)
    ax1.plot(t, s1)
    ax1.set_ylabel('S1', **yprops)

    axprops['sharex'] = ax1
    axprops['sharey'] = ax1
    ax2 = fig.add_axes([0.1, 0.3, 0.8, 0.2], **axprops)
    ax2.plot(t, s2)
    ax2.set_ylabel('S2', **yprops)

    ax3 = fig.add_axes([0.1, 0.3, 0.8, 0.2], **axprops)
    ax3.plot(t, s4)
    ax3.set_ylabel('S3', **yprops)


    ax4 = fig.add_axes([0.1, 0.1, 0.8, 0.2], **axprops)
    ax4.plot(t, s4)
    ax4.set_ylabel('S4', **yprops)

    for ax in ax1, ax2, ax3:
        p.setp(ax.get_xticklabels(), visible=False)
    p.show()


def manipulating_transforms:
    t = arange(0.0, 2.0, 0.01)
    
    signals = s1,s2,s3,s4,s5,s6,s7
    for sig in signals:
        sig = sig-mean(sig)


#=========================================================================================

if __name__ == '__main__':
#    draw_normalpdf()
#    draw_boltzman()
#    draw_boltzman_filled()
    multi_axes()
