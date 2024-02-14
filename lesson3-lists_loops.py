list = [1, 5, 9, 7, 5, 3, 2, 4, 8, 6, 12, 65, 78]

list2 = [1, 2, 3, 4]

# adding somethign to each value
for item in list:
    print(item + 5)

# converting to a string and adding another string
for item in list:
    print(str(item) + " EUR")

# inserting an item from one list into specific place in another list
for item in list2:
    list.insert(3, item)

print(list)

print(8 in list)

list_of_one = [5]
