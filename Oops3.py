class cricket: (#creating the class)

    def indplayers(self): (#defining the methods in the class, here self if the object which we are passing)
        print("sachin", 10, "mumbai")
        print("sehwag", 00, "Delhi")

    def aussie(self):
        print("smith", 12, "new south wales")
        print("starc", 19, "sydney")



info = cricket() #we are mentioning that this info is an object of computer
cricket.indplayers(info)   #calling the function here bt we hv written the class inside the class
cricket.aussie(info)       # so need to mention the class also before callling the function
                           # here (info) is an argument which is going into self


info.indplayers()           #another way of callling the function
info.aussie()
