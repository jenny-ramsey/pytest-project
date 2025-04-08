from lib.gratitudes import *

def test_initially_output_is_an_empty_gratitude():
    gratitude = Gratitudes()
    assert gratitude.format() == "Be grateful for: "

def test_output_is_an_added_gratitude():
    gratitude = Gratitudes()
    gratitude.add("peace")
    assert gratitude.gratitudes == ["peace"]

def test_output_is_an_appended_gratitude_and_formatted():
    gratitude = Gratitudes()
    gratitude.add("peace")
    assert gratitude.format() == "Be grateful for: peace"