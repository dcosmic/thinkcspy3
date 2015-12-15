import sys


def is_factor(f, n):
    if isinstance(f, int) and isinstance(n, int):
        if n % f == 0:
            return True
        else:
            return False
    else:
        return None


def is_multiple(f, n):
    return is_factor(n, f)


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
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))

test_suite()  # Here is the call to run the tests
