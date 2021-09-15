import numpy as np

#https://numpy.org/doc/stable/user/numpy-for-matlab-users.html
a = np.arange(15).reshape(3,5)
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(type(a))
print('*----------------------------------------------*')
#Array Creation
b = np.array([6,7,8,9,10])
print(b)
print(type(b))
print('*----------------------------------------------*')
b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b)
print('*----------------------------------------------*')
# Create array with complex numbers
c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)
print(type(c))

print('*----------------------------------------------*')
#Array with all zeros number
zero = np.zeros((3, 4))
print(zero)
print('*----------------------------------------------*')
#Array with all ones 
ones = np.ones((2, 3, 4), dtype=np.int16)
print(ones)
print('*----------------------------------------------*')
#Empty Array with random values from memory
empty = np.empty((2, 3))
print(empty)
print('*----------------------------------------------*')
#Create sequence of array,  create sequences of numbers
seq = np.arange(10,50,5)
print(seq)

print('*----------------------------------------------*')
#
d1 = np.arange(6)
print(d1)

print('*----------------------------------------------*')
d2 =  np.arange(12).reshape(4, 3)  
print(d2)

print('*----------------------------------------------*')
d3 = np.arange(24).reshape(2, 3, 4)
print(d3)

#Basic operations
print('*----------------------------------------------*')
a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(a-b)

