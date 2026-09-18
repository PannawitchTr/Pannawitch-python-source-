"""
โจทย์ 1: เครื่องคำนวณอย่างปลอดภัย
เขียนโปรแกรมตัวเลข 2 จำนวนและตัวดำเนินการ 1 ตัวได้แก่ + - * / แล้วแสดงผลลัพธ์
โปรแกรมต้องจัดการกรณีต่อไปนี้
    ผู้ใช้กรอกข้อมูลที่ไม่ใช่ตัวเลข #ValueError
    ผู้ใช้เือกตัวดำนินกรอื่นนอกเหนือจาก + - * /  raise ValueError
    ผู้ใช้พยายามหารด้วยศูนย์ #ZeroDivisionError
    โปรแกรมต้องแสดง จบการทำงาน เสมอด้วย finally

    ตัวอย่างผลลุพธ์ที่คาดหวัง

    ตัวเลขที่ 1: 10
    ตัวเลขที่ 2: 0
    เครื่องหมาย (+, -, *, /): /

    ไม่สามารถหารด้วยศูนย์ได้
    จบการทำงาน

"""


try:
    num1 = float(input("ใส่ตัวเลขที่ 1: "))
    num2 = float(input("ใส่ตัวเลชที่ 2: "))
    operator = input("ใส่เครื่องหมาย: ")
    result = 0
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        raise ValueError("เครื่องหมายต้องเป็น +, -, *, /")
    print(f"ผลลัพธ์: {result}")
except ValueError as error:
    print(f"กรุณากรอกตัวเลขให้ถูกต้อง {error}")

except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")

finally: 
    print("จบการทำงาน")