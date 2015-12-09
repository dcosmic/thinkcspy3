import sys

DayList = ["Sunday", "Monday", "Tuesday",
           "Wednesday", "Thursday", "Friday", "Saturday"]


def day_add(Day, delta):
    new_day = (day_num(Day) + delta) % 7
    return day_name(new_day)


def day_name(N):
    if N in range(7):
        return DayList[N]
    else:
        return None


def day_num(Day):
    if Day in DayList:
        return DayList.index(Day)
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
    test(day_add("Monday", 4) == "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")


test_suite()  # Here is the call to run the tests
