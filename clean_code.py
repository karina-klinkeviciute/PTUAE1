from typing import List

x = 1
y = x**2

z = (x + y) + (x - y)

if (x > 5) and (x % 2 == 0):
    print("x is larger than 5 and can be divided by 2")

my_list = [1, 2, 3]

print(x, y)

item = my_list[2]

my_tuple = (1,)

var1 = 5
var2 = 6
some_long_variable = 7

my_bool = 6 > 5
if my_bool:
    print("6 is bigger than 5")


def func(
    arg_one: str,
    arg_two: str,
    arg_three: str,
    arg_four: str,
    arg_five: str,
    arg_six: str,
    arg_seven: str,
    arg_eight: str,
    arg_nine: str,
    arg_ten: str,
):
    pass


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        pass

    def func2(self):
        pass


def calculate_variance(number_list: List[float]) -> float:
    sum_list = 0
    for number in number_list:
        sum_list = sum_list + number
    mean = sum_list / len(number_list)

    sum_squares = 0
    for number in number_list:
        sum_squares = sum_squares + number**2
    mean_squares = sum_squares / len(number_list)

    return mean_squares - mean**2
