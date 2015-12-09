import sys

Calender = dict(January=31, February=28, March=31, April=30,
                May=31, June=30, July=31, August=31,
                September=30, October=31, November=30, December=31)


def days_in_month(month):
    if month in Calender:
        return Calender[month]
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
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    test(days_in_month("xxx") == None)


test_suite()  # Here is the call to run the tests
