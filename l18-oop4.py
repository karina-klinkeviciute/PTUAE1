class Rectangle:
    def __init__(self, length, breadth, colour):
        self.length = length
        self.breadth = breadth
        self._colour = colour

    def area(self):
        return self.length * self.breadth

    def show_colour(self):
        print(self._colour)

class Square(Rectangle):
    def __init__(self, size, colour):
        super().__init__(size, size, colour)



rectangle = Rectangle(5, 6, "blue")

square = Square(5, "red")

print(square.area())
print(rectangle.area())
