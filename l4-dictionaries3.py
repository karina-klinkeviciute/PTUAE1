dictionary = {"a": 10, "b": 20, "c": 30}
dictionary2 = {"b": 100, "f": 200}

dictionary.update(dictionary2)

dictionary.update([("g", 45), ("h", 56)])

dictionary.update(a=78, b=89)

print(dictionary)

for key in dictionary:
    print(key)

for key in dictionary.keys():
    print(key)

for key, value in dictionary.items():
    print(key, value)

for value in dictionary.values():
    print(value)
