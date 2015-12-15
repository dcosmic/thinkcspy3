import sys


def is_even(n):
    if isinstance(n, int):
        if n % 2 == 0:
            return True
        else:
            return False
    else:
        return None


def is_odd(n):
    if is_even(n) == True:
        return False
    elif is_even(n) == False:
        return True
    else:
        return None


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
    test(is_odd(5) == True)
    test(is_odd(4) == False)
    test(is_odd(-3) == True)
    test(is_odd(0) == False)


test_suite()  # Here is the call to run the tests
