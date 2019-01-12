from numpy import *
a = array([
            [1,2,3],
            [4,5,6]
        ])
b = array([
            [1,2],
            [2,3],
            [3,4]
        ])

result = array([
                [0,0],
                [0,0]
            ])

for i in range(len(a)):                             # itterating through a
    for j in range(len(b[0])):                      # itterating through row of b
        for k in range(len(b)):                     # itterating through coloumn of b
            result[i][j] += a[i][k]*b[k][j]


for r in result:
    print(r)