#!/usr/bin/env python
#===========================================================================
# Numpy tutorial -- link http://wiki.scipy.org/Tentative_NumPy_Tutorial 
#===========================================================================

from numpy import *

#===========================================================================

def hello_narray():
    a = arange(15).reshape(3,5)
    row, column = a.shape
    rank = a.ndim # each item is indexed by 2 integers
    data_type = a.dtype.name
    byte_each_item = a.itemsize
    array_size = a.size

    # numpy.array (numpy.ndarray) overidden buildin array type
    b = array([6,7,8])
    print(type(b))


def create_ndarray():
    a = array([2,3,4])
    b = array([(1., 2., 3., 4.),
               (5., 6., 7., 8.)])

    # declar type explicitely
    c = array([1,2,3], dtype=complex)

    # special array
    my_size = (3,4)
    my_ones = ones(my_size, dtype=int64)
    my_zeros = zeros(my_size, dtype=int64)
    my_empty = empty(my_size)

    # create by range and interval
    start, end = (10, 20)
    my_range = arange(start, end, 0.1) # [m,n), default m=0 
    my_line = linspace(start, end, 100) # [m,n], to x-1 invervals, x points
    a = arange(24).reshape(4,6) # reshape array

    # form matrix from a function of indeces
    b = fromfunction(lambda x,y: return 10*x+y, (5,6), dtype=int)

def array_operations():
    a = arange(8)
    b = arange(1,9)

    # element wise operation
    c = a-b
    d = b**2
    e = 10*sin(a)
    f = a<3
    a += b
    my_floor = floor(a)

    reversed_a = a[::-1] 
    my_min = a.min()
    my_max = a.max()


def matrix_operations():
    A = arange(30,46).reshape(4,4)
    B = arange(31,47).reshape(4,4)

    A.shape = (4,4)

    dot(A,B)
    column_sum = A.sum(axis=0) # with same nth index
    row_sum = A.sum(axis=1)
    row_series_sum = A.cumsum(axis=1)

    # slicing
    # [xi:xj, yi:yj]
    E = A[1,2]
    C = A[0:3, 2:3]
    D = A[1, 2:3]
    F = A[...,2] # A[:,2]

    # iterate
    flat_array = A.flat

def builtin_functions():
    a = arange(5)
    ex_a = exp(a)
    sqrt_a = sqrt(a)

def etc():
    my_size = (2,3)
    a = random.random(size)

if __name__ == '__main__':
    hello_narray()
    create_ndarray()
    array_operations()
    matrix_operations()
