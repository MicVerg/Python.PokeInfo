from bank import value


def test_hello():
    assert value("hello") == "$100"

def test_ha():
    assert value("ha") == "$20"

def 