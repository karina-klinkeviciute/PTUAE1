import pickle

variable = 1000

with open("pickle_out.pkl", "wb") as pickle_file:
    pickle.dump(variable, pickle_file)

with open("pickle_out.pkl", "rb") as pickle_file:
    my_variable = pickle.load(pickle_file)

print(my_variable)

zodynas = {1: "pirmas", 2: "antras", 3: "trecias"}

with open("pickle_out.pkl", "wb") as pickle_file:
    pickle.dump(zodynas, pickle_file)

with open("pickle_out.pkl", "rb") as pickle_file:
    zodynas = pickle.load(pickle_file)

print(zodynas)

variable1 = 1
variable2 = 2
variable3 = 3

with open("pickle_out.pkl", "wb") as pickle_file:
    pickle.dump(variable1, pickle_file)
    pickle.dump(variable2, pickle_file)
    pickle.dump(variable3, pickle_file)

with open("pickle_out.pkl", "rb") as pickle_file:
    for item in range(3):
        print(pickle.load(pickle_file))

with open("pickle_out.pkl", "rb") as pickle_file:
    while True:
        try:
            print(pickle.load(pickle_file))
        except EOFError:
            break

    # variable1_new = pickle.load(pickle_file)
    # variable2_new = pickle.load(pickle_file)
    # variable3_new = pickle.load(pickle_file)
    # variable4_new = pickle.load(pickle_file)

# print(variable1_new, variable2_new, variable3_new)



# while True:
#     action = int(input("Choose: 1 - View, 2 - write, 3 - exit"))
#     if action == 1:
#         try:
#             with open("zmones.pkl", 'rb') as file:
#                 print(pickle.load(file))
#         except:
#             print("No names written")
#     if action == 2:
#         try:
#             with open("zmones.pkl", 'rb') as file:
#                 people = pickle.load(file)
#         except:
#             people = []
#         name = input("Enter new name: ")
#         people.append(name)
#         with open("zmones.pkl", 'wb') as file:
#             pickle.dump(people, file)
#     if action == 3:
#         print("Bye")
#         break


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

cars = [Car("Toyota", "prius"), Car("Nissan", "Leaf"), Car("peugeot", "2008")]

with open("pickle_out.pkl", "wb") as pickle_file:
    pickle.dump(cars, pickle_file)

with open("pickle_out.pkl", "rb") as pickle_file:
    new_cars = pickle.load(pickle_file)

print(new_cars)


