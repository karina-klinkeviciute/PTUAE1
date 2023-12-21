# nested dictionary
my_dictionary = {
    "name": "Albert",
    "surname": "Einstein",
    "occupation": {
        "role": "Professor",
        "workplace": "University of Berlin"
    },
    "languages": ["German", "Latin", "Italian", "English", "French", {"something": "a value"}]
}

# value from a dictionary inside another dictionary
print(my_dictionary["occupation"]["role"])

languages = my_dictionary["languages"]



print(languages)

# value form a list inside a dictionary
language = my_dictionary["languages"][2]

print(language)


dictionary = {"a": 10, "b": 20, "c": 30}
dictionary2 = {"e": 100, "f": 200}

# printing only keys of dictionary
print(dictionary.keys())

# printing only values of the dictionary
print(dictionary.values())

# removing (poping) item from dictionary and assigning it to some variable
value = dictionary.pop("b")

print(value)

print(dictionary)
print(dictionary2)

# adding dictionary 2 to dictionary
dictionary.update(dictionary2)

print(dictionary)

print(len(my_dictionary["languages"]))
