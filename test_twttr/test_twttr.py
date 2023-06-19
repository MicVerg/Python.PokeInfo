from twttr import shorten

def test_twitter():
    assert shorten("twitter") == "twttr"

def test_zonder():
    assert shorten("ZONDERKLINKERS") == "ZNDRKLNKRS"