from numpy import *
arr = array([12,23,34,45,3])
print(arr)
print(arr.dtype)

arr1 = linspace(0,15,16)
print(arr1)

arr2 = arange(0,15,2)
print(arr2)

arr3 = logspace(0,2,4)
print(arr3)

arr4 = zeros(5)
print(arr4)

arr5 = ones(5,int)
print(arr5)

arr6 = array([2,3,4,5,6])
arr7 = arr6 + 1
print(arr7)
arr8 = array([2,3,4,5,6])
arr9 = array([3,4,5,6,7])
print(arr8+arr9)
arr10= concatenate([arr8,arr9])
print(arr10)
arr11 = sort(arr10)
print(arr11)
print(min(arr11))
print(max(arr11))

array1 = arr11.view() # shallow changes will be available in both source and destination
print(array1)
arr11[1]= 4
print(arr11)
print(array1)

array1 = arr11.copy() # deep copy changes will be done only in source and not in destination
print(array1)
arr11[2]= 6
print(arr11)
print(array1)

m= array([1,2,3])
n=m
m[1]=4
print(m)
print(n)

