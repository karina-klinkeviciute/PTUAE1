animals = ["ferret", "Vole", "dog", "gecko"]

print(sorted(animals))
print(sorted(animals, key=str.lower))

a_string = "Hello"

a_string.lower()
len(a_string)

print(sorted(animals, key=len))

reverse = lambda s: s[::-1]



reverse("I am a string")

print((lambda s: s[::-1])("This is a string"))

print((lambda x1, x2, x3: (x1 + x2 + x3) / 3)(9, 6, 6))

print((lambda x1, x2, x3: (x1 + x2 + x3) / 3)(1.4, 1.1, 0.5))

print(callable(lambda s: s[::-1]))

print(callable(animals))

reverse_string = reverse

def reverse_len(string: str) -> int:
    return -len(string)

print(sorted(animals, key=reverse_len))

print(sorted(animals, key=lambda s: -len(s)))


def do_something(string, function):
    if not callable(function):
        print("can't do that")
    else:
        return function(string)


print(do_something("hello", reverse))


def func(x):
    return x, x ** 2, x ** 3

print(func(2))

print((lambda x: (x, x ** 2, x ** 3))(2))

print((lambda x: [x, x ** 2, x ** 3])(2))

print((lambda x: {1: x, 2: x ** 2, 3: x ** 3})(2))

print(f"reversed string: {(lambda s: s[::-1])('a string')}")


