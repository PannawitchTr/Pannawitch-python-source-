print("4. BMI Calculator:")
print("   - Ask for weight (kg) and height (m)")
print("   - Calculate: BMI = weight / (height ** 2)")
print()

#input
w = float(input("Enter weight = "))
h = float(input("Enter height = "))

#procress  
bmi = w / (h ** 2)

#output
print(f"BMI = {bmi}")  