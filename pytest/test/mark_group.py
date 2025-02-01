import pytest

@pytest.mark.unit
def test_unit_1():
    assert True

@pytest.mark.unit
def test_unit_2():
    assert True

@pytest.mark.unit
def test_unit_3():
    assert True

@pytest.mark.integration
def test_integration_1():
    assert True

@pytest.mark.integration
def test_integration_2():
    assert True

@pytest.mark.integration
def test_integration_3():
    assert True

@pytest.mark.validation
def test_validation():
    assert True
