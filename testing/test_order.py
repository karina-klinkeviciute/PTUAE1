from unittest.mock import Mock, patch

import pytest

from order import *
@patch('order.OrderProcessor', autospec=True)
def test_order_processor(mock_OrderProcessor):
    processor = mock_OrderProcessor.return_value
    processor.process_order.return_value = 50

    # processor = OrderProcessor()
    assert processor.process_order("apple", 1, 2) == 50


def test_write_log_message():
    with patch('builtins.open') as mock_open:

        write_log_message()
        print("OPEN CALLS:", mock_open.mock_calls, end="\n\n")
        file_handle = mock_open()
        print("FILE HANDLE CALLS:", file_handle.mock_calls, end="\n\n")
        mock_open.assert_called()

        print("FILE HANDLE WRITE CALLS:", file_handle.write.mock_calls, end="\n\n")
        # file_handle.write.mock_calls
        # mock_open.return_value__enter__.return_value.write.assert_called()


def test_raises_exception():
    with patch('builtins.open') as mock_open:
        mock_open.side_effect = FileNotFoundError("something")
        with pytest.raises(FileNotFoundError):
            write_log_message()


@patch('builtins.open')
def test_raises_exception2(mock_open):
    mock_open.side_effect = FileNotFoundError("something")
    with pytest.raises(FileNotFoundError):
        write_log_message()
