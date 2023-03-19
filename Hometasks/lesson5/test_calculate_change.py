import pytest
from Hometask1_lesson5.utils import calculate_change

def test_calculate_change_easy():
    price = "8000"
    paid = "5000 5000"
    result = calculate_change(price, paid)
    assert result == "1000 1000"

def test_calculate_change_hard():
    price = "5463"
    paid = "5000 5000"
    result = calculate_change(price, paid)
    assert result == "1000 1000 1000 1000 500 10 10 10 5 2"

def test_calculate_change_float():
    price = "10.34"
    paid = "10 10"
    result = calculate_change(price, paid)
    assert result == "5 2 2 0.5 0.1 0.05 0.01"

def test_calculate_change_error():
    price = "200"
    paid = "100"
    with pytest.raises(ValueError):
        calculate_change(price, paid)

def test_calculate_change_zero():
    price = "15600"
    paid = "5000 5000 5000 500 100"
    result = calculate_change(price, paid)
    assert result == "Сдача не требуется"