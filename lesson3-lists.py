my_list = [1, 2, 4, 9, 15, 2, 2, 2, 2]

string_list = ["good", "day", "we", "are", "learning", "good"]

various = ["hi", 1, 5, "code", "academy"]

item_to_append = 25

my_list.append(item_to_append)

print(my_list)

my_list.insert(2, 3)

print(my_list)

my_list.remove(9)

print(my_list)

my_list.pop(3)

print(my_list)

removed_item = my_list.pop(2)

print(my_list)

print(removed_item)

print(my_list.count(2))

print(string_list.count("good"))
