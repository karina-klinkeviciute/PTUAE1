my_dictionary = {"surname": "Klinkevičiūtė", "name": "Karina", 1: 15, (1, 2): 56, "age": 44, True: 15, "": "hi"}

print(my_dictionary["surname"])

print(my_dictionary["name"])

my_dictionary["name"] = "Asta"

print(my_dictionary["name"])

del my_dictionary["surname"]

print(my_dictionary)

my_dictionary["surname"] = "Smith"

my_dictionary["city"] = "Kaunas"

print(my_dictionary)

# print(my_dictionary[2])

