from bank import value


def test_hello():
    assert value("hello") == "$0"

def test_ha():
    assert value("ha") == "$20"

def test_nothing():
    assert value("no text here") == "$100"