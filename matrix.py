from numpy import *
arr1 = array([
    [1,2,3,4,5,6],
    [1,2,3,4,5,6]
             ])

arr2 = arr1.flatten()

arr3 = arr2.reshape(2,2,3)
print(arr3)

m = matrix('1 2 3; 2,3,4; 3,4,5')
m1 = matrix('1,2,3; 2,3,4; 3,4,5')
m2= m*m1

print(m2)