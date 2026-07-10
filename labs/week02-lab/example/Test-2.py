#print("2. Time Converter:")
#print("   - Ask user for seconds")
#print("   - Convert to hours, minutes, and remaining seconds")
#print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
#print()

#input
sec = int(input("Enter seconds: "))

#procress
hour = sec // 3600
sec_remain = sec % 3600
min =  sec_remain // 60
sec_remain = min % 60

#output
print(f"Time : {sec} = {hour} hour, {min} minute, {sec_remain} seconds")