
def count(list):

    even = 0
    odd = 0

    for i in list:

        if i%2 == 0:
            even = even + 1

        else:
            odd = odd + 1
    return even, odd



list = [12,23,34,45]
even, odd = count(list)
print(even)
print(odd)