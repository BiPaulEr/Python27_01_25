import pytest

def addition(x, y):
    return x + y

@pytest.mark.parametrize("x, y, result", [(3, 4, 7), (-1, 1, 0), (6, 9, 15)])
def test_addition(x, y, result):
    assert result == addition(x, y)

@pytest.mark.skipif("sys.platform == 'win32'", reason="Pas ce test sur windows")
def test_linux():
    assert False

@pytest.mark.xfail(reason="Pas encore implemente")
def test_normal_echouer():
    assert False