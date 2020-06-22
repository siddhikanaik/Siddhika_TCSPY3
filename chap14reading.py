import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for (i, v) in enumerate(xs):
        if v == target:
            return i
    return -1

friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
#
#
# test(search_linear(friends, "Zoe") == 1)
# test(search_linear(friends, "Joe") == 0)
# test(search_linear(friends, "Paris") == 6)
# test(search_linear(friends, "Bill") == -1)
#




def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if (search_linear(vocab, w) < 0):
            result.append(w)
    return result

vocab = ["apple", "boy", "dog", "down",
                          "fell", "girl", "grass", "the", "tree"]
book_words = "the apple fell from the tree to the grass".split()

# test(find_unknown_words(vocab, book_words) == ["from", "to"])
# test(find_unknown_words([], book_words) == book_words)
# test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])
#
def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if (search_binary (vocab, w) < 0):
            result.append(w)
    return result






def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds

bigger_vocab = load_words_from_file("vocab.txt")
# print("There are {0} words in the vocab, starting with\n {1} "
#               .format(len(bigger_vocab), bigger_vocab[:6]))



def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.
    """

    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds

# test(text_to_words("My name is Earl!") == ["my", "name", "is", "earl"])
# test(text_to_words('"Well, I never!", said Alice.') ==
#                              ["well", "i", "never", "said", "alice"])






def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds

# book_words = get_words_in_book("aliceinwonderland")
# print("There are {0} words in the book, the first 100 are\n{1}".
#            format(len(book_words), book_words[:100]))

# missing_words = find_unknown_words(bigger_vocab, book_words)
# print(missing_words)




import time

t0 = time.process_time()
missing_words = find_unknown_words(bigger_vocab, book_words)
t1 = time.time()
# print("There are {0} unknown words.".format(len(missing_words)))
# print("That took {0:.4f} seconds.".format(t1-t0))
#


def search_binary(xs, target):
    """ Find and return the index of key in sequence xs """
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:   # If region of interest (ROI) becomes empty
           return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = xs[mid_index]

        print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
              .format(lb, ub, ub-lb, item_at_mid, target))

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index      # Found it!
        if item_at_mid < target:
            lb = mid_index + 1    # Use upper half of ROI next time
        else:
            ub = mid_index        # Use lower half of ROI next time


xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]
# test(search_binary(xs, 20) == -1)
# test(search_binary(xs, 99) == -1)
# test(search_binary(xs, 1) == -1)
for (i, v) in enumerate(xs):
    test(search_binary(xs, v) == i)

# t0 = time.process_time()
# missing_words = find_unknown_words(bigger_vocab, book_words)
# t1 = time.process_time()
# print("There are {0} unknown words.".format(len(missing_words)))
# print("That took {0:.4f} seconds.".format(t1-t0))

search_binary(bigger_vocab, "magic")

# search_binary(bigger_vocab, "magic")
# ROI[0:19469](size=19469), probed='known', target='magic'
# ROI[9735:19469](size=9734), probed='retailer', target='magic'
# ROI[9735:14602](size=4867), probed='overthrow', target='magic'
# ROI[9735:12168](size=2433), probed='mission', target='magic'
# ROI[9735:10951](size=1216), probed='magnificent', target='magic'
# ROI[9735:10343](size=608), probed='liken', target='magic'
# ROI[10040:10343](size=303), probed='looks', target='magic'
# ROI[10192:10343](size=151), probed='lump', target='magic'
# ROI[10268:10343](size=75), probed='machete', target='magic'
# ROI[10306:10343](size=37), probed='mafia', target='magic'
# ROI[10325:10343](size=18), probed='magnanimous', target='magic'
# ROI[10325:10334](size=9), probed='magical', target='magic'
# ROI[10325:10329](size=4), probed= 'maggot', target='magic'
# ROI[10328:10329](size=1), probed='magic', target='magic'
# 10328

from math import log
log(1000 + 1, 2)
9.967226258835993

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

test(remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9]) == [1,2,3,5,6,9])
test(remove_adjacent_dups([]) == [])
test(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]) ==
                                   ["a", "big", "bite", "dog"])
    
all_words = get_words_in_book("AliceInWonderland.txt")
all_words.sort()
book_words = remove_adjacent_dups(all_words)
print("There are {0} words in the book. Only {1} are unique.".
                      format(len(all_words), len(book_words)))
print("The first 100 words are\n{0}".
           format(book_words[:100]))




newlist = (xs + ys)
newlist.sort()

def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,test(merge([], ys) == ys)
            result.extend(ys[yi:]) # Add remaining items from ystest(merge([], []) == [])
            return result
            # And we're done.test(merge(xs, ys) == zs)
        if yi >= len(ys):          # Same again, but swap rolestest(merge(["a", "big", "cat"], ["big", "bite", "dog"]) ==
            result.extend(xs[xi:])
            return result
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1