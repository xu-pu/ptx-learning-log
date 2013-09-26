#!/usr/bin/env python
#========================================================================================
# Matplotlib tutorial 02 3D plotting 
# tutorial link -- http://wiki.scipy.org/Cookbook/Matplotlib/mplot3D
#========================================================================================

from numpy import *
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3

#========================================================================================

u = r_[0:2*pi:100j]
v = r_[0:pi:100j]
x = 10*outer(cos(u), sin(v))
y = 10*outer(sin(u), sin(v))
z = 10*outer(ones(size(u)), cos(v))

def draw_3d():
    fig = p.figure()
    ax = p3.Axes3D(fig)
    ax.plot_wireframe(x,y,z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    p.show()
    
def draw_3d_2():
    fig = p.figure()
    ax = p3.Axes3D(fig)
    ax.plot3D(ravel(x), ravel(y), ravel(z))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    fig.add_axes(ax)
    p.show()

def draw_3d_3():
    fig = p.figure()
    ax = p3.Axes3D(fig)
    ax.scatter3D(ravel(x), ravel(y), ravel(z))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    p.show()

def draw_3d_4():
    fig = p.figure()
    ax = p3.Axes3D(fig)
    ax.plot_surface(x,y,z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    p.show()

#========================================================================================

delta = 0.025
x = arange(-3.0, 3.0, delta)
y = arange(-2.0, 2.0, delta)
X, Y = p.meshgrid(x,y)
Z1 = p.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
Z2 = p.bivariate_normal(X, Y, 1.5, 0.5, 1.0, 1.0)
Z = 10.0 * (Z2 - Z1)

def draw_contour():
    fig = p.figure()
    ax = p3.Axes3D(fig)
    ax.contour3D(X,Y,Z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    p.show()
    
def draw_contour_2():
    fig = p.figure()
    ax = p3.Axes3D(fig)
    ax.contourf3D(X,Y,Z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    fig.add_axes(ax)
    p.show()

#========================================================================================

if __name__ == '__main__':
    draw_contour_2()
