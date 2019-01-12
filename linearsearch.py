pos = 0

def search(list, n):

    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True

    return False



list = [4,2,6,9,0,1,8,3]
n = 10

if search(list, n):
    print("found at", pos)
else:
    print("not Found"   )