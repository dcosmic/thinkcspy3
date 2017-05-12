import sys


def count_odd_numbers(num_list):
    counter = 0
    for i in num_list:
        if isinstance(i, int):
            if i % 2 == 1:
                counter += 1
            else:
                continue
    return counter


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
    test(count_odd_numbers([1, 2, 3, 4, 5]) == 3)
    test(count_odd_numbers([0]) == 0)


test_suite()  # Here is the call to run the tests
