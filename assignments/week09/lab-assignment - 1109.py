
def calculate_electircity_cost(units):
    cost = 0 
    utb = 0
    if 1 <= units :
        u1 = min(units, 50)
        cost = u1 * 2.50
        print(f"1-50 หน่วย: {cost} บาท")
    if 50 < units :
        u1 = min(units - 50, 50)
        cost = cost + 50 * 3
        utb = u1 * 3
        print(f"51-100 หน่วย: {utb} บาท")
    if 100 < units < 200 :
        u1 = min(units - 100, 100)
        cost = cost + (units - 100) * 3.5
        utb = u1 * 3.50
        print(f"101-200 หน่วย: {utb} บาท")
    if 200 < units:
        u1 = (units - 200)
        cost = cost + (units - 200) * 4.00
        utb = u1 * 4.00
        print(f"200 หน่วยขึ้นไป: {utb} บาท")
    print("ค่าบริการ: 25.00 บาท")
    cost += 25
    print(f"รวมค่าไฟทั้งสิ้น: {cost} บาท")

while True:
    print("==== โปรแกรมคำนวนค่าไฟฟ้า ====")
    print("1.คำนวนค่าไฟ")
    print("2.ออกจากโปรแกรม")
    choice = input("เลือกเมนู: ")
    if choice == "1":
        print()
        units = float(input("กรอกจำนวนหน่วยไฟฟ้า: "))
        print()
        calculate_electircity_cost(units)
    else:
        break