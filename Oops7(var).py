class cars:

    wheel = 4

    def __init__(self):

        self.mileage = 70
        self.brand = "BUGATTI"



c1 = cars()

c2 = cars()

c2.mileage = 80
c2.brand = "BMW"

# if we want to modify the wheel value we will use classs name not method name.
cars.wheel = 8

print(c1.mileage, c1.brand, c1.wheel)
print(c2.mileage, c2.brand, c2.wheel)