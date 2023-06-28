from numb3rs import validate
import pytest

def test_3numbers():
    assert validate("129.123.123") == False

def test_4numbers():
    assert validate("129.123.123.123") == True

def test_4numbers_false():
    assert validate("129.123.123.456") == False