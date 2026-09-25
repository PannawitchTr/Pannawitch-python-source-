"""
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