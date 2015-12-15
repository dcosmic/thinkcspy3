import sys
import math


def isnum(x):
    if isinstance(x, int) or isinstance(x, float):
        return True
    else:
        return False


def slope(x1, y1, x2, y2):
    if isnum(x1) and isnum(y1) and isnum(x2) and isnum(y2):
        if x1 == x2:
            slp == math.inf
        else:
            slp = (y2 - y1) / (x2 - x1)
        return slp
    else:
        return None


def intercept(x1, y1, x2, y2):
    if x1 < x2:
        inter = y1 - x1 * slope(x1, y1, x2, y2)
    elif x1 == x2:
        inter == None
    elif x1 > x2:
        inter = y2 - x2 * slope(x1, y1, x2, y2)
    else:
        inter = None
    return inter


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
    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)


test_suite()  # Here is the call to run the tests
