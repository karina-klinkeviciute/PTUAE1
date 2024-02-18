animals = ["ferret", "Vole", "dog", "gecko"]

print(sorted(animals))

# we can use a function (a callable) as a key in sorted function.
# In other words, we can pass a function as a parameter
print(sorted(animals, key=str.lower))

a_string = "Hello"

a_string.lower()
len(a_string)

# passing another function as a parameter
print(sorted(animals, key=len))

reverse = lambda s: s[::-1]

reverse("I am a string")

# defining a lambda function and calling it right away
print((lambda s: s[::-1])("This is a string"))

print((lambda x1, x2, x3: (x1 + x2 + x3) / 3)(9, 6, 6))

print((lambda x1, x2, x3: (x1 + x2 + x3) / 3)(1.4, 1.1, 0.5))

# checking if something is callable
print(callable(lambda s: s[::-1]))

print(callable(animals))

# we can assign a function to a variable and then use that variable as that
# function too. In other words, we are renaming a function
reverse_string = reverse

# reversed length. Length with a - added to it
def reverse_len(string: str) -> int:
    return -len(string)

# When we are sorting by
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

# lambda function inside a lambda function
print((lambda x, y: (x * (lambda s: s+15)(y)))(5, 6))

adding_numbers = (lambda x, y: x + y)(13, (lambda num: num + 15)(15))
print(adding_numbers)

print(
    (lambda numb1, numb2: numb1 * numb2)(
        numb1=(lambda numb: numb + 15)(numb=0), numb2=(lambda numb: numb + 15)(numb=0)
    )
)
