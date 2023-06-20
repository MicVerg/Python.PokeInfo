from fuel import convert, gauge

def test_convert_string():
    with pytest.raises(ValueError):
        convert("cat")