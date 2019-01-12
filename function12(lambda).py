from functools import reduce

def even(nums):
    return nums%2==0

def square(list):
    return list**2
def sum(a,b):
    return a + b




nums = [1,2,3,4,5,6,7,8,9]

evens = list(filter(even,nums))

print(evens)

squares = list(map(square,evens))
print(squares)

sums = reduce(sum,squares)
print(sums)

