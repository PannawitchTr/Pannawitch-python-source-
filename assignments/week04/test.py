# รับชื่อจริง (หรือข้อความ) จากผู้ใช้
# นับจำนวนสระทั้งหมดในข้อความนั้นว่ามีกี่ตัว(a,A,e,E,i,I,o,O,u,U)

# ตัวอย่างหน้าจอ
# What is your name?: Boonchoo
# Your text have 4 vowels.
"""วิธีที่1 
name = input("What is your name?: ")
letter = list(name)
print(letters)

a = letters.count('a')
e = letters.count('e')
i = letters.count('i')
o = letters.count('o')
u = letters.count('u')

A = letters.count('A')
E = letters.count('E')
I = letters.count('I')
O = letters.count('O')
U = letters.count('U')

count = a + e + i + o + A + E + I + O + U
print("Your text have", count, "vowels")
"""
#วิธีที่ 2 for loop
name = input("What is your name?: ")

lower_name = name.lower # if don't want to write upper vowels
for letter in name:
    if letter == 'a' or letter == 'A':
        count = count + 1
    elif letter == 'e' or letter == 'E':
        count = count + 1
    elif letter == 'i' or letter == 'I':
        count = count + 1
    elif letter == 'o' or letter == 'O':
        count = count + 1
    elif letter == 'u' or letter == 'U':
        count = count + 1
    print("Your text have", count, "vowels")


#วิธีที่3 if in
name = input("What is your name?: ")
#lower_name = name.lower
if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
    print("Your text have", count, "vowels")
