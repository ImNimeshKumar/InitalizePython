def search(list, n):
    l = 0
    u = len(list)-1

    while l < u:
        mid = (l+u) // 2
        if list[mid] == n:
            return True
        else:
            if n < list[mid]:
                u = mid
            else:
                l = mid











list = [1,2,3,4,5,6,7,8,9]
n = 2
if search(list, n):
    print("found")
else:
    print("not found")