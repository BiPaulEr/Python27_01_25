import pytest

def test_simple():
    assert 1 + 1 == 2
    assert 1 in [1, 2, 3]
    assert isinstance(1, int)
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        1/0
    