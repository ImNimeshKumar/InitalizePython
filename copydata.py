df = open("fetch data", "r")

wf = open("newfile", "w")
for i in df:
    wf.write(i)