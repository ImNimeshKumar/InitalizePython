# passing a list checking it is mutable or not and as it is modifying the original list so it is mutable.

def update(x):
    print(id(x))

    x[0] = 85
    print(x)
    print(id(x))


a = [10, 23, 34]
update(a)

print(id(a))

print(a)