def countodd(list):
    count = 0
    for i in list:
        if i % 2 != 0:
            count = count + 1
    return count

list = [10, 11, 12, 13, 14, 15, 16]

print(countodd(list))










