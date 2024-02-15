from typing import Generator


def simple_generator(n: int) -> Generator[int, None, None]:
    for i in range(n):
        yield i


for value in simple_generator(5):
    print(value)


def infinite_range(start: int = 0) -> Generator[int, None, None]:
    current = start
    while True:
        yield current * 2
        current += 1


counter = 0
for value in infinite_range(10):
    print(value)
    counter += 1
    if counter == 1000:
        break


def count_up_to(x: int) -> Generator[int, None, None]:
    count = 1
    while count <= x:
        yield count
        count += 1


for number in count_up_to(5):
    print(number)

# print(count_up_to(5))
# count_up_to(5).send(3)
# print(count_up_to(5))


from typing import Generator
# def my_generator() -> Generator[int, None, None]:
#     for i in range(5):
#         received_value = yield i
#         print(f"Received value: {received_value}")
#
# gen = my_generator()
# for value in gen:
#     print(f"Received: {value}")
#     gen.send("Hello")  # Sending a value to the generator

# going to the next yield each time the generator is called
def generator():
    yield 1
    yield 2
    yield 3


for value in generator():
    print(value)

# generator expression (similar to list iteration, only doesn't store all results in memory)
numbers = (x for x in range(10))

for number in numbers:
    print(number)

# underscore is a convention when we don't need a value that a function, a generator or a method returns
for _ in range(20):
    print("hi")

my_dictionary = {1: 2, 2: 23, 3: 4, 4: 5}

for _, value in my_dictionary.items():
    print(value)

def my_function():
    return 1, 2

result, _ = my_function()

print(result)

print(isinstance(5, int | float))

