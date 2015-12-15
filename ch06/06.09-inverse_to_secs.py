import sys


def hours_in(s):
    if isinstance(s, int):
        hrs = s / 60 / 60
        return int(hrs)
    else:
        return None


def minutes_in(s):
    if isinstance(s, int):
        mins = s / 60 - 60 * hours_in(s)
        return int(mins)
    else:
        return None


def seconds_in(s):
    if isinstance(s, int):
        secs = s - 60 * minutes_in(s) - 60 * 60 * hours_in(s)
        return secs
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
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)


test_suite()  # Here is the call to run the tests
