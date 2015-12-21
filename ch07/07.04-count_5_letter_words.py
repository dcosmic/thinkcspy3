import sys


def count_5_letter_words(word_list):
    count = 0
    for i in word_list:
        if len(i) == 5:
                count += 1
        else:
            continue
    return count


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(count_5_letter_words(['abandon', 'count', 'close', 'live', 'a', 'wonder']) == 2)
    test(count_5_letter_words(['0']) == 0)


test_suite()  # Here is the call to run the tests
