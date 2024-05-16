from unittest.mock import Mock, patch

from order import *
@patch('order.OrderProcessor', autospec=True)
def test_order_processor(mock_OrderProcessor):
    processor = mock_OrderProcessor.return_value
    processor.process_order.return_value = 50

    # processor = OrderProcessor()
    assert processor.process_order("apple", 1, 2) == 50
