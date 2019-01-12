df = open("yuvraj.jpg", "rb")
print(df.read())

im = open("image.jpg", "wb")
for data in df:
    print(data)