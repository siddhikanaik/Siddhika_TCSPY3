import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)



xs = [1, 2, 5, 5, 8]
ys = [2, 8, 11]
def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] == ys[yi]:
            result.append(xs[xi])
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            xi += 1
        else:
            yi += 1
        print(result)

test(merge(xs, ys) == [2, 8])
test(merge([1, 3, 4, 5, 5], [1, 2, 4, 5, 6]) == [2, 3, 5, 6])


def merge2(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            return result          # And we're done.

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1

        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1

        else:
            yi += 1
        print(result)

test(merge2(xs, ys) == [1, 5, 5])
test(merge2([1, 3, 4, 5, 5], [1, 2, 4, 5, 6]) == [2, 3, 5, 6])


def merge3(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result          # And we're done.

        if yi >= len(ys):
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1

        elif xs[xi] < ys[yi]:
            xi += 1

        else:
            result.append(ys[yi])
            yi += 1
        print(result)

test(merge3(xs, ys) == [11])
test(merge3([1, 3, 4, 5, 5], [1, 2, 4, 5, 6]) == [2, 3, 5, 6])

def merge4(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result          # And we're done.

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1

        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1

        else:
            result.append(ys[yi])
            yi += 1
        print(result)

test(merge4(xs, ys) == [1, 5, 5, 11])
test(merge4([1, 3, 4, 5, 5], [1, 2, 4, 5, 6]) == [2, 3, 5, 6])