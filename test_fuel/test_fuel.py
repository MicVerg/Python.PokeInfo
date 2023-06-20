from fuel import convert, gauge
import pytest

def test_convert_string():
    with pytest.raises(ValueError):
        convert("cat")