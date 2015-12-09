import sys

def turn_clockwise(direction):
	if direction == "N":
		new_direction = "E"
	elif direction == "E":
		new_direction = "S"
	elif direction == "S":
		new_direction = "W"
	elif direction == "W":
		new_direction = "N"
	else:
		new_direction = None
	return new_direction

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
	test(turn_clockwise("N") == "E")
	test(turn_clockwise("W") == "N")
	test(turn_clockwise(42) == None)
	test(turn_clockwise("rubbish") == None)

test_suite() # Here is the call to run the tests