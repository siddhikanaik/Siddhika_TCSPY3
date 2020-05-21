def add5(add_list):
    count = 0
    for i in add_list:
        if i % 2 != 0:
            count += i
        else:
            return count
    return count



add_list = [4, 7, 13, 14, 15, 16]

print(add5(add_list))