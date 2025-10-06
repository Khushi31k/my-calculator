"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, divide, subtract, multiply

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add(-2, -3) == -5
        assert add(-10, 5) == -5
        assert add(5, -10) == -5

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert subtract(-5, -3) == -2   # (-5) - (-3) = -2
        assert subtract(-10, 5) == -15
        assert subtract(5, -10) == 15

# TODO: Students will add TestMultiplyDivide class
class TestMultiplyDivide:
    def test_multiply_positive_numbers(self):
        assert multiply(3,4) == 12
        assert multiply(7,8) == 56

    def test_multiply_by_zero(self):
        assert multiply(5,0) == 0
        assert multiply(0,10) == 0

    def test_multiply_negative_numbers(self):
        assert multiply(-2,3) == -6
        assert multiply(-4,-5) == 20

    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5
    
    def test_divide_negative_numbers(self):
        assert divide(-10, 2) == -5
        assert divide(-12, -3) == 4
