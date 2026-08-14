"""
เขียน FUNCTION แปลงหน่วยสกุลเงิน ที่สามารถแปลงเงินจาก
THB <-> USD 1 USD = 32 THB
THB <-> JPY 100 JPY = 22 THB

โดยใช้ชื่อและการใช้งาน
function convert_currency(100, "USD")

แสดงผลออกทางหน้าจอ
100 THB = 3.3 USD

และทดสอบการใช้งาน function ที่ตัวเองเขียน
"""

def convert_currency(convert_to, currency):
    if convert_to == "1":
        convert = currency / 32 # this can remove to used another way next comment
        print(f"{currency} THB = {convert:.2f} USD") #print(f"{currency} THB = {currency / 32:.2f} USD")
    elif convert_to == "2":
        convert = currency * 32
        print(f"{currency} USD = {convert:.2f} THB")
    elif convert_to == "3":
        convert = (currency/22) * 100
        print(f"{currency} THB = {convert:.2f} JPY")
    elif convert_to == "4":
        convert = (currency/100) * 22
        print(f"{currency} JPY = {convert:.2f} THB")
    else:
        print("Invalid")

print("Convert Currency:")
print("1.Convert THB to USD")
print("2.Convert USD to THB")
print("3.Convert THB to JPY")
print("4.Convert JPY to THB")
convert_to = input("Enter number convert currency: ")
currency = float(input("Enter money to exchange: "))
convert_currency(convert_to, currency)

"""Simple print
def convert_currency(a, b):
    if b == "USD":
        print(f"{a} THB = {a / 32} USD")
    else:
        print(a "USD" =, a * 32, "THB")

convert_currency(100, "USD")
convert_currency(100, "THB")
"""