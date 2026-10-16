"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""

def get_temperatures():
    temps = [37, 38, 30, 29, 40, 25, 33]#list
    return temps

def analyze_temps(temp_list):
    average = sum(temps) / 7
    high = max(temps)
    low = min(temps)

    return (average, high, low)#tuple

def display_analysis(avg, high, low):#ในวงเล็บเป็นคนละตัวกับใน temps เพราะมันเป็น local ใช้กับช่องเดียวกันเท่านั้น
    print("Temperature Analysis for the Week:")
    print("Average: %.1f"% avg)#altway print(f"Average: {avg}")
    print("highest: %.1f"% high)
    print("Lowest: %.1f"% low)

temps = get_temperatures()
print(temps)
result = analyze_temps(temps)
print(result)
display_analysis(result[0], result[1], result[2])