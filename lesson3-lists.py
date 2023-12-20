from pprint import pprint

my_list = [1, 2, 4, 9, 15, 2, 2, 2, 2]

string_list = ["good", "day", "we", "are", "learning", "good"]

# we can have a list of different types variables
various = ["hi", 1, 5, "code", "academy"]

my_list.append(45)

item_to_append = 25

# we can use a variable inside a function call
my_list.append(item_to_append)

print(my_list)

# inserts numbber 3 at a position of index 2
my_list.insert(2, 3)

print(my_list)

# removes a value 9 from the list
my_list.remove(9)

print(my_list)

# removes the element with index of 3 from the list
my_list.pop(3)

print(my_list)

# removes an element with an index 2 from the list and assigns it to "removed_item"
removed_item = my_list.pop(2)

print(my_list)

print(removed_item)

print(my_list.count(2))

print(string_list.count("good"))

# adds teo lists
new_list = string_list + my_list

print(new_list)

# also adds two lists
my_list.extend(various)

print(my_list)

# adds a list inside another list
my_list.append(string_list)

print(my_list)

# prints a value from a list inside a list
print(my_list[13][2])

pprint(my_list)

