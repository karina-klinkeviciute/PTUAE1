from typing import Union


# print(some_variable)
def my_dummy_int_func(a: Union[str, float]) -> None:
    try:
        int_value = int(a)
        return int_value
    except ValueError as exc:
        print(exc.args)
    except TypeError:
        print('Type of "a" is incompatible; should either be a number or a string')


print(my_dummy_int_func("d"))
