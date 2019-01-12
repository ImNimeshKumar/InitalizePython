class cricket:
    def __init__(self, name, number):
        self.name = name
        self.number = number



    def indplayers(self):
        print("Details are", self.name, self.number)


info1 = cricket("sachin", 10)
info2 = cricket("sehwag", 00)


info1.indplayers()
info2.indplayers()

