from fuel import convert, gauge
import pytest

def test_convert_string():
    with pytest.raises(ValueError):
        convert("cat")

def test_convert_y0():
    with pytest.raises(ZeroDivisionError):
        convert("-1 / 0")

def test_convert_40():
    assert convert("40 / 100") == 40

def test_convert_80():
    assert convert("80 / 100") == 80

def test_gauge_1():
    assert gauge(int("1")) == 'E'

def test_gauge_99():
    assert gauge(int("99")) == 'F'

def test_gauge_50():
    assert gauge(int("50")) == '50%'