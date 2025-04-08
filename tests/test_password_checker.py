import pytest
from lib.password_checker import *

def test_valid_password_returns_true():
    checker = PasswordChecker()
    assert checker.check("StrongPassword1") == True

def test_password_exactly_8_characters():
    checker = PasswordChecker()
    assert checker.check("Password") == True

def test_short_password_raises_exception():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check("short")
    assert str(e.value) == "Invalid password, must be 8+ characters."

def test_empty_password_raises_exception():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check("")
    assert str(e.value) == "Invalid password, must be 8+ characters."