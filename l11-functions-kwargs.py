def are_adults(reason, **kwargs):
    print(reason)
    for name, age in kwargs.items():
        # print(key, value)
        if age < 18:
            return False
    return True


print(are_adults("night club", jonas=25, tadas=15, lina=36))

print(are_adults("sell cigarettes", petras=19, dovydas=21))

# def integer_division(num_one=10, num_two=2):
#     return num_one // num_two
#
# print(integer_division(num_two=2, num_one=10))