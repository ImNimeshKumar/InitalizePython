name = input("enter your name ")
if name == "kohli" or "nimesh":
    print("so you are " + name + " enter the password then")
    pwd = input("enter the password ")
    if pwd == "virat18":
        print("Access Granted")
    else:
        print("access denied because of incorrect password")
else:
    print("only kohli can conquer this pitch")
