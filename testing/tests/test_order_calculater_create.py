# ===========Test creation==================
import pytest

from testing.order_calculator import OrderCalculator


def test_create_order_calculator():
    order_calculator = OrderCalculator()
    assert order_calculator is not None


def test_create_order_calculator_items_empty():
    order_calculator = OrderCalculator()
    items = order_calculator._items
    assert items == []


def test_create_order_calculator_get_items_empty():
    order_calculator = OrderCalculator()
    items = order_calculator.get_items()
    assert items == []
