x = int(input("enter the number"))

for i in range(0, x):
    if i%3==0 and i%5==0:
        continue

    else:
        print(i)