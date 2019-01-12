from array import *
values = array("i",[2,4,7,1,9])

arr = array(values.typecode, (a for a in values))

for i in arr:
    print(i)
