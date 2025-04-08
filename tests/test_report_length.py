from lib.report_length import report_length

def test_short_string():
    result = report_length("Hi")
    assert result == "This string was 2 characters long."

def test_long_string():
    result = report_length("This is a long string")
    assert result == "This string was 21 characters long."

def test_empty_string():
    result = report_length("")
    assert result == "This string was 0 characters long."

def test_whitespace_string():
    result = report_length("   ")
    assert result == "This string was 3 characters long."

def test_mixed_whitespace_and_text():
    result = report_length(" Hello ")
    assert result == "This string was 7 characters long."

def test_special_characters():
    result = report_length("!$&&!")
    assert result == "This string was 5 characters long."

def test_numeric_string():
    result = report_length("12345")
    assert result == "This string was 5 characters long."

