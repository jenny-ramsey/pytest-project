from lib.counter import *

""" Initially reports a count of zero
"""

def test_counter_initially_reports_zero():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."

"""When we add a single number to the counter it is reflected in the final count
"""

def test_adds_a_single_number_to_the_count():
    counter = Counter()
    counter.add(4)
    result = counter.report()
    assert result == "Counted to 4 so far."

""" When we add a single number and then another single number it is reflected in the final count
"""
def test_adds_two_numbers_to_the_count():
    counter = Counter()
    counter.add(2)
    counter.add(3)
    result = counter.report()
    assert result == "Counted to 5 so far."

""" When we add a single number, then another single number and then a third number 
it is reflected in the final count
"""

def test_adds_three_numbers_to_the_count():
    counter = Counter()
    counter.add(3)
    counter.add(2)
    counter.add(3)
    result = counter.report()
    assert result == "Counted to 8 so far."