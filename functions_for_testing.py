def division(a, b):
    return a / b


def love6(a: int, b: int) -> bool:
    return a == 6 or b == 6 or a + b == 6 or a - b == 6


assert love6(1, 2) == False, "Must be False: neither arg is 6, nor is the sum or subtraction equal to 6"
assert love6(5, 6) == True, "Must be True: second arg is 6"
assert love6(1, 5) == True, "Must be True: 1 + 5 = 6"
assert love6(12, 12) == False, "Must be False: neither arg is 6, nor is the sum or subtraction equal to 6"
assert love6(13, 7) == True, "Must be True, because 13 - 7 = 6"

print("tests done")


# funcs.py
def reverse_string(text: str) -> str:
    """Reverses the order of any given string.

    Throws a TypeError on inputs that are not strings.
    """
    # Some implementation here
    if isinstance(text, str):
        return text[::-1]
    else:
        raise TypeError("This only accepts strings")
    # return text[::-1]


from functions_for_testing import division, reverse_string


def test_division():
    assert division(4, 2) == 2


def test_division_negatives():
    assert division(4, -2) == -2


def test_division_by_zero():
    try:
        division(1, 0)
        assert False, "Should raise ZeroDivisionError"
    except ZeroDivisionError:
        pass


def test_reverse_string():
    string = "string for test"
    assert reverse_string(string) == "tset rof gnirts"


def test_reverse_string_abc():
    string = "abc"
    assert reverse_string(string) == "cba"


def test_reverse_string_numbers():
    string = "abc123"
    assert reverse_string(string) == "321cba"


def test_reverse_string_wrong_type():
    try:
        reverse_string(5)
        assert False, "it should raise a TypeError if the argument is not a string"
    except TypeError:
        pass


def test_reverse_string_none():
    try:
        reverse_string(None)
        assert False, "it should raise a TypeError if the argument is not a string"
    except TypeError:
        pass


def test_reverse_string_list():
    try:
        reverse_string([1, 2, 3])
        assert False, "it should raise a TypeError if the argument is not a string"
    except TypeError:
        pass


if __name__ == "__main__":
    # test_division()
    # test_division_by_zero()
    # test_division_negatives()
    test_reverse_string()
