available = 10

x = int(input("enter the number of mango you want "))

i = 1
while i <= x:
    if i > available:
        print("we are out of stock")
        break

    print("mango")
    i = i+1
print("come again")