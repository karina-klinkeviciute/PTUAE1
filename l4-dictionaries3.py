dictionary = {"a": 10, "b": 20, "c": 30}
dictionary2 = {"b": 100, "f": 200}

# Wys to update a dictionary
dictionary.update(dictionary2)

dictionary.update([("g", 45), ("h", 56)])

dictionary.update(a=78, b=89)

print(dictionary)


# iterating through keys of dictionary
for key in dictionary:
    print(key)

# another way
for key in dictionary.keys():
    print(key)

# iterating through items (keys and values)
for key, value in dictionary.items():
    print(key, value)

# iterating through values
for value in dictionary.values():
    print(value)

my_list = []

my_list = list()

my_dict = {}

my_dict = dict()


# "zipping" lists and creating a dictionary from them
keys = ["Albert", "Tom", "Stephen"]
values = [1, 4, 5]
new_dictionary = dict(zip(keys, values))

print(new_dictionary)
