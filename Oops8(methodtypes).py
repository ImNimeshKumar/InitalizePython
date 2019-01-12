class student:

    school = "Dharam public school"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3



    @classmethod
    def info(cls):
        return cls.school


    def staticmethod():
        print("this is staticmethod which has nothing to do with classmethod or instancemethod")


c1 = student(32, 34, 67)
c2 = student(34, 45, 56)
c3 = student(89, 67, 54)


print(c1.average())
print(c2.average())
print(c3.average())

print(student.info())

student.staticmethod()