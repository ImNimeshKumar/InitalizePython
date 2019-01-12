class student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()   #object is inside outer class

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()


    class laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = "8gigs"

        def show(self):
            print(self.brand, self.cpu, self.ram)




s1 = student("kohli", 18)
s2 = student("sahcin", 10)

s1.show()
