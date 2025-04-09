from lib.house import House

"""As a user
So that I can build my dream home
I want to be able to make a house from a blueprint having two floors.

As a user
So that I can remember key details about my house
I want to be able to store and see the house number, floor count and door colour.

As a user
So that I can make my house my own
I want to be able to change the door colour.
"""

# When we build a new house
# It needs to be given a house number and starting door colour
# Those and the number of floors are stored in attributes
def test_house_attributes():
    house = House(137, "white")
    assert house.floors == 2
    assert house.number == 137
    assert house.door_colour == "white"

# When we have a house
# The key details can be got back
def test_get_details():
    house = House(137, "white")
    assert house.get_details() == "House number 137 has 2 floors and a white door"

# When we have a house
# And we change its door colour
# This is reflected in its attribute
def test_repaint_door():
    house = House(24, "red")
    house.repaint_door("blue")
    assert house.door_colour == "blue"

