# with using the third variable

a = 10
b = 20
temp = b
b = a
a = temp
print(a,b)


# without using third variable

c = 1
d = 2
c = c + d
d = c - d
c = c - d
print(c, d)

# using XOR

c = 1
d = 2
c = c ^ d
d = c ^ d
c = c ^ d
print(c, d)




