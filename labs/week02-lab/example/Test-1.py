#print("Now try these exercises:")
#print()
#print("1. Circle Calculator:")
#print("   - Ask user for radius")
#print("   - Calculate area (π * r²)")
#print("   - Calculate circumference (2 * π * r)")
#print("   - Use 3.14159 for π")
#print()

#input
r = float(input("Enter radius: "))

#procress
area = 3.14159 * r ** 2
cirucumference = 2 * 3.14159 * r

#output
print(f"Area = {area}, Cirucumference = {cirucumference}") #or print("Area of this circle =", area) or ("circumference of this circle =" + str(circumference))