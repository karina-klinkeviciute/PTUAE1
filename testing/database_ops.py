import datetime
import time


def filter_db_by() -> list:
    # Simulate an expensive database operation
    time.sleep(20)
    data = [
      { "name": "apples", "price": 10.34 },
      { "name": "oranges", "price": 55.55 },
      { "name": "grapes", "price": 6.1 },
    ]
    return data


def is_weekday():
    today = datetime.datetime.today()
    # .weekday() returns an integer: 0 is Monday, 6 is Sunday
    return 0 <= today.weekday() < 5
