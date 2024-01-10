def multiply(x, y):
    return x * y

print(multiply(2, 4))

multiply = lambda x, y: x*y

print(multiply(2, 4))

# def uppercase(word):
#     return word.upper()

print(list(map(lambda word: word.upper(), ['cat', 'dog', 'cow'])))

