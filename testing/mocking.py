from unittest.mock import patch
from using_database_ops import sum_price_products


@patch('using_database_ops.is_weekday', autospec=True)
@patch('using_database_ops.filter_db_by', autospec=True)
def test_sum_price_products(mock_filter_db_by, mock_is_weekday):

    mock_filter_db_by.return_value = [
      { "name": "stuff", "price": 12.45 },
      { "name": "more_stuff", "price": 16.6 },
    ]
    mock_is_weekday.return_value = True
    result = sum_price_products()
    assert result == 12.45 + 16.6

