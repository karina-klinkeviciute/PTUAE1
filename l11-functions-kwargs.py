def are_adults(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


print(are_adults(jonas=25, tadas=15, lina=36))

print(are_adults(petras=15, dovydas=21))

# def integer_division(num_one=10, num_two=2):
#     return num_one // num_two
#
# print(integer_division(num_two=2, num_one=10))