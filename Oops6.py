class details:
    def __init__(self):
        self.name = "nimesh"
        self.age = 28

    def update(self):
       self.age = 30

    def compare(self, whometocompare):
        if self.age == whometocompare.age:
            return True
        else:
            return False

c1 = details()


c2 = details()

c2.age = 23


print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)



if c1.compare(c2):
    print("they are same")
else:
    print("they are different")







