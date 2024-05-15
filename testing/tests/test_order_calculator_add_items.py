import pytest

from testing.order_calculator import OrderCalculator


# =============Test adding items===================

def test_order_calculator_add_one_item():
    order_calculator = OrderCalculator()
    item = ("Apple", 1.5, 5)
    order_calculator.add_item(item)

    assert order_calculator._items == [item]


def test_order_calculator_add_multiple_items():
    order_calculator = OrderCalculator()
    item1 = ("Apple", 1.5, 5)
    item2 = ("Pear", 2.5, 2)
    item3 = ("Plum", 0.5, 6)
    order_calculator.add_item(item1)
    order_calculator.add_item(item2)
    order_calculator.add_item(item3)

    assert order_calculator._items == [item1, item2, item3]


def test_order_calculator_raises_no_quantity():
    order_calculator = OrderCalculator()
    item1 = ("Apple", 1.5)

    with pytest.raises(ValueError):
        order_calculator.add_item(item1)


def test_order_calculator_raises_name_none():
    order_calculator = OrderCalculator()
    item = (None, 2, 5)
    with pytest.raises(ValueError):
        order_calculator.add_item(item)


def test_order_calculator_raises_price_none():
    order_calculator = OrderCalculator()
    item = ("Orange", None, 5)
    with pytest.raises(ValueError):
        order_calculator.add_item(item)


def test_order_calculator_raises_quantity_none():
    order_calculator = OrderCalculator()
    item = ("Orange", 2, None)
    with pytest.raises(ValueError):
        order_calculator.add_item(item)
