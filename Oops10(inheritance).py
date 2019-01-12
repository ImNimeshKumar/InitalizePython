class A:
    def feature1(self):
        print("feature 1 is in A")
    def feature2(self):
        print("feature 2 is in A")
class B:
    def feature3(self):
        print("feature 3 is in A")

    def feature4(self):
        print("feature 4 is in A")
class C(A,B):
    def feature5(self):
        print("feature 3 is in A")



a1 = A()
b1 = B()
c1 = C()

b1.feature1()
b1.feature2()


c1.feature5()
c1.feature4()
c1.feature3()
c1.feature2()
c1.feature1()