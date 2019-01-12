#Factorial using python

def factorial(x):

    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


result = factorial(7)
print(result)