def countlength5(list):
    count = 0
    for i in list:
        if len(i) == 5:
            count = count + 1
    return count

list = ["since", "Sudii", "dog", ]

print(countlength5(list))


