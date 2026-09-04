'''
print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = 'Hello World'
for letter in text:
    if letter == 'l':
        count += 1
print(f"{count} letters 'l' found in '{text}'")
'''
# รับค่า text ของผู่ใช้
# รับค่าอักขรที่ต้องการค้นหาจากผู้ใช้
# แสดงผลจำนวนของอักขระในข้อความ text

# ตัวอย่างหน้าจอ
# Insert your text: Boonchoo Jitnupong
# Character to find: o
# 5 letters 'o' found in 'Boonchoo jitnupong'
'''
count = 0
text = input("Intert your text: ")
char = input("Character to find: ")
for letter in text:
    if letter == char:
        count += 1
print(f"{count} letter '{char}' found in '{text}'")
'''

# เขียนโปรแกรมตรวจสอบความแข็งแรงของ PASSWORD
# นิยามของ strong password คือ ยาวมากกว่า 8 ตัว, มีอักขระ @, มีตัวเลช, มีตัวอักษร
# ตัวอย่างหน้าจอ
# Insert your password: Boonchoo
# Your password is not strong!
'''
password = input("Insert your password: ")
lenght = len(password)
words = password.split('@')
left = words[0].isalnum()
right = words[1].isalnum()

if len(words) > 1 and password.count('@') == 1:
    left = words[0].isalnum()
    right = words[1].isalnum()
else:
    left = False;
    right = False;

if lenght >= 8 and password.count('@') == 1: and left == True and right == True:
    print("Your password is strong!")
else:
    print("Your password is not strong!")
'''
