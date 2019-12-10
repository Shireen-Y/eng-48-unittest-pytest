from sci_calc import *


def test_find_sqrt():
    assert find_sqrt(100) == 10.0, 'Did not find the square root'


def test_find_ceil():
    assert find_ceil(12.2) == 13