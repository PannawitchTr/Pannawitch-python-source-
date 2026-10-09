""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Vehicle info: Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_door):
        super().__init__(brand, model, year)
        self.number_of_door = number_of_door

    def get_info(self):
        return f"Veheicle info: Brand: {self.brand}. Model: {self.model}, Year: {self.model}, Number of doors: {self.number_of_door}"

vehicle = Vehicle("Apple","Iphone pro max", "2026")
print(vehicle.get_info())

car = Car("Apple","Iphone pro duo", "2026", "2")
print(car.get_info())

"""
Write a Python class Rectangle with:

privae attributes for length and width
Methods to calculate area (getArea() and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def getArea(self):
        return f"Area of {self.__length} length and {self.__width} width = {self.__width * self.__length}"

    def getPerimeter(self):
        return f"Perimeter of {self.__length} length and {self.__width} width = {2* (self.__length + self.__width)}"

    def isSquare(self):
        return self.__width == self.__length 

Rec = Rectangle(5, 10)
print(Rec.getArea())
print(Rec.getPerimeter())
print(Rec.isSquare())