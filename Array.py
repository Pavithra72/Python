from array import *
#import array as arr

vals = array('i',[5,3,6,8,-9,2,5])
vals.reverse()
print(vals)
for i in range(len(vals)):
    print(vals[i])
newArr = array(vals.typecode, (a*a for a in vals))
newArr.pop(2)
for e in newArr:
    print(e)

n = int(input("Enter the size "))
arr = array('i', [])
for e in range(n):
    value = int(input("Enter the Value "))
    arr.append(value)

for e in arr:
    print(e)

searchVal = int(input("Enter the value to search"))
k =0
for e in arr:
    if searchVal == e:
        print(k)
    k=k+1
print(arr.index(searchVal))