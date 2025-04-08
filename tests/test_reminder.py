
from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Jenny")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Jenny!"

# We would typically have a number of these examples.
