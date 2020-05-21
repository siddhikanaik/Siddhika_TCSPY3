import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno  # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)







def mysum(xs):
    """Sum all the numbers in the list xs, and return the total. """
    running_total = 0
    for x in xs:
        running_total = running_total + x
    return running_total

def test_suite():
    test(mysum([1, 2, 3, 4]) == 10)
    test(mysum([1.25, 2.5, 1.75]) == 5.5)
    test(mysum([1, -2, 3]) == 2)
    test(mysum([ ]) == 0)
    test(mysum(range(11)) == 55) # 11 is not included in the list.


# def sum_to(n):
# """ Return the sum of 1+2+3 ... n """
#     ss = 0
#     v = 1
#     while v <= n:
#         ss = ss + v
#         v = v + 1
#     return ss

def print_multiples(n):
    for i in range(1, 7):
        print(n * i, end="   ")
    print()
for i in range(1, 7):
    print_multiples(i)

def print_mult_table():
    for i in range(1, 7):
        print_multiples(i)

print_mult_table()
# test_suite()
