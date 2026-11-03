import pytest
from pizza_order import pizza_price, order_discount, delivery_status

# Test cases aimed at line (statement) coverage: every line runs at least once.

# Starter test cases
def test_plain_medium_pizza():
    assert pizza_price("medium", 0, False) == 350

def test_on_time_delivery():
    assert delivery_status(20, 3) == "on time"


# pizza_price
def test_unknown_size_raises():
    with pytest.raises(ValueError, match="unknown size"):
        pizza_price("extra large", 1, False)

def test_negative_toppings_raises():
    with pytest.raises(ValueError, match="invalid toppings"):
        pizza_price("medium", -1, False)

def test_more_than_three_toppings():
    # 500 + 3*40 + 2*30
    assert pizza_price("large", 5, False) == 680

def test_cheese_burst_small_raises():
    with pytest.raises(ValueError, match="cheese burst not available for small"):
        pizza_price("small", 1, True)

def test_cheese_burst_medium():
    # 350 + 2*40 + 100
    assert pizza_price("medium", 2, True) == 530


# order_discount
def test_discount_below_minimum_total():
    assert order_discount(250, "tuesday", True) == 0

def test_discount_tuesday_student():
    assert order_discount(600, "tuesday", True) == 350

def test_discount_weekend_student():
    assert order_discount(600, "saturday", True) == 50

def test_discount_weekday_student():
    assert order_discount(600, "monday", True) == 110


# delivery_status
def test_not_deliverable():
    assert delivery_status(20, 12) == "not deliverable"

def test_late_delivery():
    assert delivery_status(40, 5) == "late"

def test_free_pizza():
    assert delivery_status(50, 5) == "free pizza"
