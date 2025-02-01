import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4]

def test_ficture_simple(sample_data):
    assert sum(sample_data) == 10

def test_ficture_simple_2(sample_data):
    assert sum(sample_data) == 10

liste_data = [1, 2, 3]
@pytest.fixture(params= liste_data)
def liste_int_data(request):
    return request.param

@pytest.fixture(params= ["A", "B", "C"])
def liste_str_data(request):
    return request.param

def test_liste_int_data(liste_int_data, liste_str_data):
    print(liste_int_data)

def test_liste_int_data(liste_int_data):
    print(liste_int_data)