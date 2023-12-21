my_set = {2, 5, 8}

print(my_set)

my_set = {2, 5, 8, 5, 2}

print(my_set)

my_list = [23, 56, 89, 12, 45, 78, 12, 78, 56]

# make a set from a list
my_set = set(my_list)

print(my_set)

# add element
my_set.add(100)

print(my_set)

# remove element
my_set.remove(100)

print(my_set)

# remove element and assign it to a value
value = my_set.pop()

print(my_set)

print(value)
