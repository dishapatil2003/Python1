#Define a circle class to create Circle with radius r using the constructor.
#Define an area() method of the class which calculates the area of the circle.
#Define a perimeter() mathod of the class which allows you to calculate the perimeter of the circle.

class Circle:
    def __init__(self , radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())  # Output: 132.84 133.92