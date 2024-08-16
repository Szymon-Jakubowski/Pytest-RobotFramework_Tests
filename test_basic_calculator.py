import pytest
from basic_calculator import Calculator

@pytest.fixture
def calculator() -> Calculator:
    """
    Fixture to provide a fresh Calculator instance for each test.
    """
    return Calculator()

def test_add(calculator):
    assert calculator.add(5) == 5
    assert calculator.add(-3) == 2
    assert calculator.add(0) == 2

def test_subtract(calculator):
    assert calculator.subtract(3) == -3
    assert calculator.subtract(-2) == -1
    assert calculator.subtract(0) == -1

def test_multiply(calculator):
    calculator.add(1)  # set initial value to 1
    assert calculator.multiply(5) == 5
    assert calculator.multiply(-2) == -10
    assert calculator.multiply(0) == 0

def test_divide(calculator):
    calculator.add(10)  # set initial value to 10
    assert calculator.divide(2) == 5
    assert calculator.divide(-5) == -1
    with pytest.raises(ValueError):
        calculator.divide(0)

def test_reset(calculator):
    calculator.add(5)
    calculator.reset()
    assert calculator.get_value() == 0.0

def test_chaining_operations(calculator):
    calculator.add(10)
    calculator.subtract(2)
    calculator.multiply(3)
    calculator.divide(4)
    assert calculator.get_value() == 6.0

@pytest.mark.parametrize("initial, add_value, subtract_value, expected", [
    (0, 5, 3, 2),
    (10, -5, 5, 0),
    (1, 0, 1, 0),
    (100, 50, 150, 0),
])
def test_parametrized_operations(initial, add_value, subtract_value, expected):
    calc = Calculator(initial)
    calc.add(add_value)
    calc.subtract(subtract_value)
    assert calc.get_value() == expected

def test_floating_point_operations(calculator):
    calculator.add(0.1)
    calculator.add(0.2)
    assert calculator.get_value() == pytest.approx(0.3, rel=1e-9)
