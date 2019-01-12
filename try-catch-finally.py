a = 10
b = 2



try:
    print("resource open")
    print(a / b)
    k = int(input("enter the number"))
    print(k)

except ZeroDivisionError as e:
    print("you cannot divide the number with zero", e)

except ValueError as v:
    print("invalid input", v)
except Exception as e:
    print("unexpected behaviour")

finally:
    print("resource closed")