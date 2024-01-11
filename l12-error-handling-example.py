from typing import Union


def my_dummy_int_func(a: Union[str, float]) -> None:
    try:
        int_value = int(a)
        return int_value
    except ValueError:
        print('Value of "a" cannot be deduced to integer')
    except TypeError:
        print('Type of "a" is incompatible; should either be a number or a string')

print(my_dummy_int_func({1, 2}))
