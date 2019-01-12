count = 0
def recursion():

    global count
    count = count + 1
    print(count, "hello")
    recursion()

recursion()
#So bydefault recursion will go till 996 step