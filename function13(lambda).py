from functools import reduce

num = [1,2,3,4,5,6,7,8,9]

evens = list(filter(lambda n : n%2==0, num))
print(evens)

squares = list(map(lambda n : n**2, evens))
print(squares)

sum = reduce(lambda a,b : a+b, squares)
print(sum)