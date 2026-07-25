"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese

"""
weight = float(input("Enter weight(kg): "))
height = float(input("Enter height(m): "))
bmi = weight / (height ** 2)
print(f"{bmi}")
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Normal weight")
elif 25.0 <= bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")

"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
print("Currency Converter Choose Conversion Direction")
print("1.THB to USD")
print("2.USD to THB")
choice = int(input("Enter Conversion Direction Number: "))
if choice == 1:
    amount = float(input("Enter amount:"))
    money = amount / 35.5
    print(f"total amount: {money:.2f} USD")
    print(f"Formula: {amount} / {35.5} = {money:.2f} USD")
elif choice == 2:
    amount = float(input("Enter amount:"))
    money = amount * 35.5
    print(f"Formula: {amount} * {35.5} = {money:.2f} THB")
else:
    print("Invalid")
