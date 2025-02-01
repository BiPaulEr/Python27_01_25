import pytest
from calculator import *

def test_add():
    assert add(2, 3) == 5
def test_check_value():
    assert check_value(15) == "Big"  
    #assert check_value(5) == "Small"
def test_multiply():
    assert multiply(2, 3) == 6