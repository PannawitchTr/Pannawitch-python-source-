"""
    สร้าง class Rectangle โดยกำหนดให้
    - มี attribute ชื่อ length และ width ที่เก็บข้อมูลความยาวและความกว้างของสี่เหลี่ยม
    - มี method ชื่อ get_area() ที่คืนค่าพื้นที่ของสี่เหลี่ยม
    - มี method ชื่อ get_perimeter() ที่คืนค่ารอบรูปของสี่เหลี่ยม
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to get the area
    def get_area(self):
        self.area = self.length * self.width #alternative way (return self.length * self.width)
        return f"คืนค่าพื้นที่ของสี่เหลี่ยม = {self.area}"
        

    # Method to get the perimeter
    def get_perimeter(self):
        self.permimeter = 2 * (self.width + self.length) #alternative way (retrun f"Perimeter = {self.length} * {self.width} = {2 * (self.length * self.width)}"")
        return f"คืนค่ารอบรูปของสี่เหลี่ยม = {self.permimeter}"

rect = Rectangle(10, 5)
print(rect.get_area())       # Should print 50
print(rect.get_perimeter())  # Should print 30

"""
ขอให้เขียนคลาส Circle ที่ทำงานคล้ายกับคลาส Rectangle

"""

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return f"radius = 2 * 3.14 * {self.radius} = {2 * 3.14 * self.radius}"

rect = Circle(10)
print(rect.get_radius()) 