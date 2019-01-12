class student:
    def __init__(self, m1, m2):
        self. m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):

        s = 0
        if a!=None and b!=None and c!=None:
            c=a+b+c
        elif a!=None and b!=None:
            c=a+b
        else:
            c=a
        return c


s1 = student(1,1)
print(s1.sum(1,2,3))