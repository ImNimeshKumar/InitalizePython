#to change the limit of 996 steps we us sys module

import sys


sys.setreucrsionlimit(1500)

print(sys.getrecursionlimit())

count = 0
def recursion():

    global count
    count = count + 1
    print(count, "hello")
    recursion()

recursion()