import sys


def isnum(x):
    if isinstance(x, int) or isinstance(x, float):
        return True
    else:
        return False


def to_secs(h, m, s):
    if isnum(h) and isnum(m) and isnum(s):
        secs = h * 60 * 60 + m * 60 + s
        return int(secs)
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
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433, 0, 0) == 8758)


test_suite()  # Here is the call to run the tests
