import pytest
from pizza_order import pizza_price, order_discount, delivery_status

# Test cases aimed at branch coverage: every decision is taken both True and False.

# Starter test cases
def test_plain_medium_pizza():
    assert pizza_price("medium", 0, False) == 350

def test_on_time_delivery():
    assert delivery_status(20, 3) == "on time"


# pizza_price
def test_unknown_size_raises():
    # size not in SIZE_PRICE -> True
    with pytest.raises(ValueError, match="unknown size"):
        pizza_price("extra large", 1, False)

def test_negative_toppings_raises():
    # toppings < 0 -> True
    with pytest.raises(ValueError, match="invalid toppings"):
        pizza_price("medium", -1, False)

def test_zero_toppings_boundary():
    # toppings < 0 -> False at the boundary
    assert pizza_price("small", 0, False) == 200

def test_exactly_three_toppings():
    # toppings > 3 -> False at the boundary
    assert pizza_price("small", 3, False) == 320

def test_more_than_three_toppings():
    # toppings > 3 -> True: 500 + 3*40 + 2*30
    assert pizza_price("large", 5, False) == 680

def test_four_toppings_boundary():
    # toppings > 3 -> True at the boundary: 350 + 3*40 + 1*30
    assert pizza_price("medium", 4, False) == 500

def test_cheese_burst_small_raises():
    # is_cheese_burst -> True, size == "small" -> True
    with pytest.raises(ValueError, match="cheese burst not available for small"):
        pizza_price("small", 1, True)

def test_cheese_burst_medium():
    # is_cheese_burst -> True, size == "small" -> False
    assert pizza_price("medium", 2, True) == 530

def test_cheese_burst_large():
    assert pizza_price("large", 4, True) == 750


# order_discount
def test_discount_below_minimum_total():
    # order_total < 300 -> True
    assert order_discount(250, "tuesday", True) == 0

def test_discount_at_minimum_total():
    # order_total < 300 -> False at the boundary
    assert order_discount(300, "monday", False) == 30

def test_discount_tuesday_student():
    assert order_discount(600, "tuesday", True) == 350

def test_discount_tuesday_non_student():
    assert order_discount(600, "tuesday", False) == 300

def test_discount_saturday_non_student():
    assert order_discount(600, "saturday", False) == 0

def test_discount_sunday_student():
    assert order_discount(600, "sunday", True) == 50

def test_discount_weekday_student():
    assert order_discount(600, "monday", True) == 110

def test_discount_weekday_non_student():
    # is_student -> False
    assert order_discount(455, "friday", False) == 45


# delivery_status
def test_not_deliverable():
    # distance_km > 10 -> True
    assert delivery_status(20, 12) == "not deliverable"

def test_exactly_ten_km_deliverable():
    # distance_km > 10 -> False at the boundary
    assert delivery_status(10, 10) == "on time"

def test_exactly_thirty_minutes_on_time():
    assert delivery_status(30, 5) == "on time"

def test_late_delivery():
    # minutes_taken <= 30 -> False, <= 45 -> True
    assert delivery_status(40, 5) == "late"

def test_exactly_forty_five_minutes_late():
    assert delivery_status(45, 5) == "late"

def test_free_pizza():
    # minutes_taken <= 45 -> False
    assert delivery_status(50, 5) == "free pizza"
