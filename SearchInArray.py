
from array import *

arr = array("i",[])

val = int(input("enter the length of the array"))

for i in range(val):
    x = int(input("enter the next values"))
    arr.append(x)



print(arr)

x = int(input("enter the element which need to be search"))

a = 0
for e in arr:
    if e == x:

        print(a)
    a = a + 1



# Search with the function

print(arr.index(x))



