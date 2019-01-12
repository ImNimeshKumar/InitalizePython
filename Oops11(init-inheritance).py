class A:
    def __init__(self):
        print("this in init A")

    def feature1(self):
        print("feature 1 is in A")
    def feature2(self):
        print("feature 2 is in A")

class B(A):
    def __init__(self):
        super().__init__()
        print("this in init B")

    def feature3(self):
        print("feature 3 is in A")

    def feature4(self):
        print("feature 4 is in A")

    def feat(self):
        super().feature2()

a1 = B()
a1.feat()



