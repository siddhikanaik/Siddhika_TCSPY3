test(did_pass):
"""  Print the result of a test.  """
linenum = sys._getframe(1).f_lineno  # Get the caller's line num
if did_pass:
    msg = "Test at line {0} ok.".format(linenum)
else:
    msg = ("Test at line {0} FAILED.".format(linenum))
print(msg)

search_linear(xs, target):
""" Find and return the index of target in sequence xs """
for (i, v) in enumerate(xs):
    if v == target:
        return i
return -1


def remove_adjacent_dups(xs):
    """ Return a new list in which all adjacent
        duplicates from xs have been removed.
    """
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e

    return result


test(remove_adjacent_dups([1, 2, 3, 3, 3, 3, 5, 6, 9, 9]) == [1, 2, 3, 5, 6, 9])
test(remove_adjacent_dups([]) == [])
test(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]) ==
     ["a", "big", "bite", "dog"])

