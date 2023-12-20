list = [1, 5, 9, 7, 5, 3, 2, 4, 8, 6, 12, 65, 78]

list2 = [1, 2, 3, 4]

for item in list:
    print(item * item)

for item in list2:
    list.insert(3, item)

print(list)

print(8 in list)
