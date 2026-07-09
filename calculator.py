# Static variable
tax_rate = 0.05

# Dynamic variable
price = float(input("Enter price: "))

total = price + (price * tax_rate)

print("Total:", total)