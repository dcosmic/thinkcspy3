import sys

DayList=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def day_name(N):
	if N in range(7):
		return DayList[N]
	else:
		return None

def test(did_pass):
	""" Print the result of a test. """
	linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
	if did_pass:
		msg = "Test at line {0} ok.".format(linenum)
	else:
		msg = ("Test at line {0} FAILED.".format(linenum))
	print(msg)

def test_suite():
	""" Run the suite of tests for code in this module (this file).
	"""
	test(day_name(3) == "Wednesday")
	test(day_name(6) == "Saturday")
	test(day_name(42) == None)

test_suite() # Here is the call to run the tests