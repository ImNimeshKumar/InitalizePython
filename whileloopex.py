i = 0
j = 0
n = int(input("enter the number for which you want to find the sum "))
while i < n:
    i = i+1
    j = j+i
    print("the sum of natural number is", j)
    if j % 2 == 0:
        print(j)
    else:
        print("back off")
