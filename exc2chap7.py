def addeven(list):
    count = 0
    for i in list:
        if i % 2 == 0:
            count = count + i
    return count

list = [10, 11, 12, 13, 14, 15, 16]

print(addeven(list))
