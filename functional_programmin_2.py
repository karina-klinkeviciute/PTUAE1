# def reverse(s):
#     return s[::-1]

# reverse("I am a string")

animals = ["cat", "DOG", "hedgehog", "gecko"]

# iterator = map(reverse, animals)

# map applies some function to each item of an iterable (for example list)
iterator = map(lambda s: s[::-1], animals)

print(list(map(lambda s: s[::-1], ["cat", "dog", "hedgehog", "gecko"])))

# print(list(map(lambda s: s[::-1], ["cat", "dog", "hedgehog", 3.14, "gecko"])))

# map()


# for item in iterator:
#     print(item)

print(list(iterator))

# map used with more parameters - as many as the parameters of function it calls
def f(a, b, c):
    return a + b + c

print(list(map(f, [1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 2])))


# in filter, the function needs to return either True or False
def greater_than_100(x):
    return x > 100

print(list(filter(greater_than_100, [1, 123, 54, 456, 78, 489])))

def is_upper(s):
    return s.isupper()

print("".join(list(filter(is_upper, "acbABC"))))

list(range(10))


def is_even(x):
    return x % 2 == 0

print(list(filter(is_even, range(10))))

print(list(filter(lambda s: s.isupper(), animals)))

print(list(filter(lambda x: x % 2 == 0, range(10))))


def f(x, y):
    return x + y

from functools import reduce

print(reduce(f, [1, 2, 3, 4, 5]))

sum([1, 2, 3, 4, 5])

def multiply(x, y):
    return x * y


def factorial(n):
    return reduce(multiply, range(1, n + 1))


print(factorial(5))

print(factorial(6))

from math import factorial

print(factorial(4))

def greater(x, y):
    return x if x > y else y


print(reduce(greater, [45, 12, 89, 25], 10))

print(reduce(f, [1, 2, 3, 4, 5], 100))

numbers = [1, 2, 3, 4, 5]

print(list(map(str, numbers)))


# rewriting map using reduce
def custom_map(function, iterable):

    return reduce(
        lambda items, value: items + [function(value)],
        iterable,
        []
    )

print(list(custom_map(str, numbers)))

