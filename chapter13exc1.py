def exercise1():
    with open('text.txt', 'w') as t:
        t.write('first\n')
        t.write('snake\n')
        t.write('third')

    with open('exercise1.txt', 'w') as t:
        for line in reversed(list(open('text.txt'))):
            t.write(line.rstrip())
            t.write('\n')

print(exercise1())

