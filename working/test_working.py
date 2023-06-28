from working import new_format, convert
import pytest

def test1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test2():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test3():
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"


def test4():
    with pytest.raises(ValueError):
        convert("7 AM - 8 AM")


def test5():
    with pytest.raises(ValueError):
        convert("16 AM - 17 AM")


def test6():
    with pytest.raises(ValueError):
        convert("9:99 AM - 10:61 AM")