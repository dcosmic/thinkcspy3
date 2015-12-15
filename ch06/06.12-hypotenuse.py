import sys
import math


def isnum(x):
    if isinstance(x, int) or isinstance(x, float):
        return True
    else:
        return False


def hypotenuse(a, b):
    if isnum(a) and isnum(b):
        return math.sqrt(a ** 2 + b ** 2)
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
    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)


test_suite()  # Here is the call to run the tests
