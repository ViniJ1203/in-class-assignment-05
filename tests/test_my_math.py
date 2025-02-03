import pytest

from src.my_math import sum, multiply, difference, absolute_sum, calculate_birth_year

def test_sum():
    res = sum(1,1)
    assert res == 2

# Work together
## Test multiply
def test_multiply():
    res = multiply(2,2)
    assert res == 4 

# Check for understanding
## Test difference
def test_difference():
    res = difference(3,3)
    assert res == 0
# Work together
## Test absolute sum
def test_it_should_return_positive_numbers():
    res = absolute_sum(1,2)
    assert res == 3

def test_it_should_return_positive_numbers_2():
    res = absolute_sum(1,3)
    assert res == 4

# Check for understanding
## Test calculate age
def test_calc_age():
    res = calculate_birth_year(2010, 40, True )
    assert res == 1970

