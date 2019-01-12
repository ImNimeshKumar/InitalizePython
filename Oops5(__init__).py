class myclass:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = self.firstname+ " " +self.lastname
        print("constructor has been called")





object = myclass("nimesh", "kumar")
print(object.lastname)
print(object.firstname)
print(object.fullname)



