#!/usr/bin/env python
#========================================================================================
# 3D plotting with python matplotlib
#========================================================================================

from numpy import *
import matplotlib.pyplot as plt
import pylab as p
from  mpl_toolkits.mplot3d import Axes3D

#========================================================================================
# z = 10 * x * y
#========================================================================================

u = r_[0:10:100j]
v = r_[0:10:100j]

x1 = outer(u, ones(size(v)))
y1 = outer(ones(size(v)), v)
z1 = 10*outer(u, v)

#========================================================================================

def draw_scatter():    
    fig = p.figure()
    ax = Axes3D(fig)
    ax.scatter3D(x1,y1,z1)
    p.show()

def draw_wireframe():
    fig = p.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(x1,y1,z1)
    p.show()

def draw_surface():
    fig = p.figure()
    ax = Axes3D(fig)
    ax.plot_surface(x1,y1,z1)
    p.show()

def draw_trisurf():
    fig = p.figure()
    ax = Axes3D(fig)
    # convert into 1D array
    ax.plot_trisurf(ravel(x1),ravel(y1),ravel(z1))
    p.show()
    
def draw_contour():
    fig = p.figure()
    ax = Axes3D(fig)
    ax.contour(x1,y1,z1)
    p.show()

def draw_contourf():
    fig = p.figure()
    ax = Axes3D(fig)
    ax.contourf(x1,y1,z1)
    p.show()


if __name__ == '__main__':
    pass
