import sys


def count_words_up_to_sam(word_list):
    count = 0
    for i in word_list:
        if i != 'sam':
            if isinstance(i, str):
                count += 1
        else:
            break
    if count == len(word_list):
        return None
    else:
        return count+1
    

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
    test(count_words_up_to_sam(['abandon', 'count', 'close', 'live', 'sam', 'wonder']) == 5)
    test(count_words_up_to_sam(['0']) == None)


test_suite()  # Here is the call to run the tests
