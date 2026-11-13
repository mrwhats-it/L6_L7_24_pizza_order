from hypothesis import given, strategies as st
from pizza_order import toppings_price, pizza_inches, split_bill, TOPPINGS, SIZES

@given(st.text() | st.none())
def test_toppings_price_no_crash(s):
    try:
        toppings_price(s)
    except Exception as e:
        assert False, f"toppings_price crashed with: {e!r}"

@given(st.text() | st.none())
def test_pizza_inches_no_crash(s):
    try:
        pizza_inches(s)
    except Exception as e:
        assert False, f"pizza_inches crashed with: {e!r}"

@given(st.text() | st.none())
def test_split_bill_no_crash(s):
    try:
        split_bill(s)
    except Exception as e:
        assert False, f"split_bill crashed with: {e!r}"

# Valid inputs (any case, extra spaces) must still give the right answer
@given(st.lists(st.sampled_from(sorted(TOPPINGS)), min_size=1),
       st.sampled_from(["", " ", "  "]), st.booleans())
def test_toppings_price_valid(toppings, pad, upper):
    csv = ",".join(pad + (t.upper() if upper else t) + pad for t in toppings)
    assert toppings_price(csv) == sum(TOPPINGS[t] for t in toppings)

@given(st.sampled_from(sorted(SIZES)), st.sampled_from(["", " ", "\t"]), st.booleans())
def test_pizza_inches_valid(size, pad, lower):
    text = pad + (size.lower() if lower else size) + pad
    assert pizza_inches(text) == SIZES[size]

@given(st.integers(min_value=0, max_value=10**9), st.integers(min_value=1, max_value=10**6))
def test_split_bill_valid(total, people):
    assert split_bill(f"{total}/{people}") == round(total / people, 2)

# Invalid inputs must be rejected (None), not silently priced
@given(st.text().filter(lambda s: any(t.strip().lower() not in TOPPINGS for t in s.split(','))))
def test_toppings_price_rejects_unknown(s):
    assert toppings_price(s) is None

@given(st.integers(max_value=0))
def test_split_bill_rejects_bad_people(people):
    assert split_bill(f"100/{people}") is None
