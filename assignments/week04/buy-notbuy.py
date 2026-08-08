prices = []
total = 0
items = []
budget = 0
remain = 0
print("Enter prices of 6 items:")
for i in range(1, 7):
    price = int(input(f"Item {i}: "))
    prices.append(price)


budget = int(input("\nEnter total budget: "))

for price in prices:
    if total + price <= budget:
        print(f"\nItem {i} = {price} -> buy")
        total += price
        items.append(price)
    else:
        print(f"\nItem {i} = {price} -> cannot buy")

    print(f"Current total = {total}")

print(f"\nBought items: {items}")
print(f"Total spent: {total}")
remain = budget - total
print(f"Remaining budget: {remain}")