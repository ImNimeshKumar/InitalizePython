from time import sleep
from threading import *


class A(Thread):
    def function1(self):
        for i in range(10):
            print("hello")
            sleep(.5)

class B(Thread):
    def function2(self):
        for i in range(10):
            print("hi")
            sleep(.5)


a1 = A()
b1 = B()

b1.function2()

a1.function1()

print("main thread executing this")