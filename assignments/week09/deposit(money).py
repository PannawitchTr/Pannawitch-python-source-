def deposit(money):
    print(f"ยอดเงินเริ่มต้น: {money} บาท")
    
    try:
        raw_input = input("กรอกจำนวนเงินที่ต้องการฝาก: ")
        
        amount = float(raw_input)
        
        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
            
        balance = money + amount

    except ValueError as error:
        if "could not convert" in str(error):
            print("\nเกิดข้อผิดพลาด: กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น")
        else:
            print(f"\nเกิดข้อผิดพลาด: {error}")
            
    else:
        print("\nฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {balance:.2f} บาท")
        
    finally:
        print("สิ้นสุดรายการฝากเงิน")

deposit(1000)