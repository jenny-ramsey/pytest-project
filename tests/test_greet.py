from lib.greet import *

def test_greets_person_of_given_name():
    result = greet("Jenny")
    assert result == "Hello, Jenny!"