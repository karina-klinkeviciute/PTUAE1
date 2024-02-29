from functools import reduce

print(reduce(lambda a, b: a if a > b else b, [1, 2, 3, 4, 5, 8, 1, 3]))


print(max([1, 2, 3, 4, 5, 8, 1, 3]))
