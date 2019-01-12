def factorial(x):
    fact = 1

    for i in range (1,x+1):
        fact = fact*i

    return fact



n = 7
result = factorial(n)
print(result)