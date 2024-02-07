a = str(5)

# if a > b :

print("hi" > "hello")

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __eq__(self, other):
        if isinstance(other, Car):
            if self.make == other.make and self.model == other.model and self.year == other.year:
                return True
        return False


car1 = Car("Toyota", "Prius", 2010)
car2 = Car("Toyota", "Prius", 2010)
car3 = Car("Nissan", "Leaf", 2020)

if car1 == car3:
    print("They are the same car")
else:
    print("Those are different cars")

"Hello" + "World"

class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, int):
            return Vector(self.x + other, self.y + other)
        raise TypeError(f"unsupported operand type(s) for +: 'Vector' and '{type(other).__name__}'")

    def __radd__(self, other):
        return self.__add__(other)


    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

vector1 = Vector(5, 4)
vector2 = Vector(3, -6)

print(vector1)

print(vector2 + vector1)
print(vector1 + 5)
print(5 + vector1)





class Train:
    def __init__(self, wagons):
        self.wagons = wagons

    def __len__(self):
        return self.wagons

train = Train(5)

print(len(train))

