my_dictionary = {
    "name": "Albert",
    "surname": "Einstein",
    "occupation": {
        "role": "Professor",
        "workplace": "University of Berlin"
    },
    "languages": ["German", "Latin", "Italian", "English", "French", {"something": "a value"}]
}

print(my_dictionary["occupation"]["role"])

languages = my_dictionary["languages"]



print(languages)

language = my_dictionary["languages"][2]

print(language)

dictionary = {"a": 10, "b": 20, "c": 30}
dictionary2 = {"e": 100, "f": 200}
print(dictionary.keys())


print(dictionary.values())

value = dictionary.pop("b")

print(value)

print(dictionary)
print(dictionary2)
dictionary.update(dictionary2)

print(dictionary)

print(len(my_dictionary["languages"]))
