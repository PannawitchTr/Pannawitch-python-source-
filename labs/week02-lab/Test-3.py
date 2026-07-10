# Template 3: Shopping Calculator
#shopping_calculator = '''
# Shopping Calculator Template
#discount 10%

#input
item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

#procress
subtotal = item_price * quantity
discount_price = subtotal * discount_percent / 100
discount_comp = subtotal - discount_price
tax_amount = discount_comp * (tax_percent / 100) 
final_total = tax_amount + discount_comp

#output
print(f"Subtotal : {subtotal}, Discount price {discount_price}, Discount total {discount_comp}, Tax amount {tax_amount}, Final total {final_total}")