# does python have pass by reference or pass by value??????
# python doesnt have any of those pass by reference or pass by value

def update(x):

    print(id(x))

    x = 8
    print(x)
    print(id(x))




a = 10
update(a)
print(a)
print(id(a))
