"""
<<<<<<< HEAD
2 types of programing
1. structured programing ==> การเขียนโปรแกรมเชิงโครงสร้าง (โปรแกรมที่เขียนแบบนี้ส่วนใหญ่)> c, javascript, php, python
2. object-oriented programing(OOP) ==> การเขียนโปรแกรมเชิงวัตถุ > java, C#, python  
"""

class ClassName:
    """Class docstring"""

    #ข้อมูลที่ต้องใช้ในการแก้ปัญหา ระบุไว้ใน contructor metod
    def __init__(self, parameters):
        # Constructor method
        self.attribute = value

    #การกระทำ ==> method
    def method_name(self):
        # Instance method
        return something

    def method_name(self):
        pass

# การสร้างวัตถุจากคลาส ==> เอาคลาสมาใช้
myObj = ClassName(parameters)

#ใช้งานวัตถุจากคลาส
print(myObj.attribute)
resultFromMethod = myObj.method_name()

myObj2 = ClassName(parameters)
print(myObj2.attibute)
print(myObj2.method_name())
myObj2.method_name2()
=======
programming ==> การเขียนโปรแกรม
2 types
1) structured programming ==> การเขียนโปรแกรมเชิงโครงสร้าง ==> c, js, php, python
2) Object-Oriented Programming (OOP) ==> การเขียนโปรแกรมเชิงวัตถุ ==> java, c#, python
"""

# วิธีการ หรือแนวทางในการแก้ปัญหา template/แม่แบบ/พิมพ์เขียว/ตรายาง
class ClassName:
    """Class docstring"""
    
    # ข้อมูล ที่จำเป็นในการแก้ปัญหา
    def __init__(self, parameters):
        # Constructor method
        self.attribute = value
        self.attribute2 = value
        self.attribute3 = value
    
    # การกระทำ เพื่อแก้ปัญหา ต้องทำอะไรบ้าง
    def method_name(self):
        # Instance method
        return something
    
    def method_name2(self):
        return ...

# เริ่มใช้งานคลาส ==> สร้างวัตถุจากคลาส
myObj = ClassName(parameters)

print(myObj.attribute)
resultFromMethod = myObj.method_name()
print(myObj.method_name2())
>>>>>>> upstream/main
