import pytest
from logic import calculate  # Direct import—same folder, no package prefix

def test_add():
    assert calculate(5, 3, "+") == 8

def test_subtract():
    assert calculate(5, 3, "-") == 2

def test_multiply():
    assert calculate(5, 3, "*") == 15

def test_divide():
    assert calculate(6, 2, "/") == 3.0
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculate(5, 0, "/")

def test_sqrt():
    assert calculate(16, 0, "sqrt") == 4.0
    with pytest.raises(ValueError, match="Cannot take square root"):
        calculate(-1, 0, "sqrt")

def test_invalid_op():
    with pytest.raises(ValueError, match="Invalid operation"):
        calculate(1, 1, "invalid")

def test_exponent():
    assert calculate(2, 3, "^") == 8.0
    assert calculate(5, 2, "^") == 25.0
    assert calculate(-2, 3, "^") == -8.0  # Handles negatives