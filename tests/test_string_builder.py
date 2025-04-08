from lib.string_builder import *

# Do not need all the different tests if some of the complex tests cover the methods needed
# for example the single string and the size of a single string can be removed as these methods
# are covered in the more complex multiple strings concatenated examples.

"""Initially output is an empty string
"""

def test_initially_output_is_an_empty_string():
    string = StringBuilder()
    string.output() == "" 

"""When we add a single string the output is now that string
"""

def test_adding_a__string():
    string = StringBuilder()
    string.add("Hello")
    assert string.output() == "Hello"

"""When we add a single string then other strings the output is now those strings concatenated
"""

def test_adding_multiple_strings():
    string = StringBuilder()
    string.add("Hello")
    string.add(" ")
    string.add("world!")
    assert string.output() == "Hello world!"

"""Test for the size of a string - only one assert per test is the general rule
"""

def test_size_of_string():
    string = StringBuilder()
    string.add("Goodnight, world!")
    assert string.size() == 17

"""Test for the size of multiple strings concatenated
"""
def test_size_of_concatenated_strings():
    string = StringBuilder()
    string.add("Hello")
    string.add(" ")
    string.add("world!")
    assert string.size() == 12