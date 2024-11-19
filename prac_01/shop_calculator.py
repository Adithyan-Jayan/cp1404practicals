"""
CP1404/CP5632 - Practical
Shop Calculator
"""
# Input: Number of items
number_of_items = int(input("Enter the number of items: "))

# Initialize total price to 0
total_price = 0

# Loop to input the price of each item
for i in range(number_of_items):
    price = float(input(f"Enter the price of item {i+1}: $"))
    total_price += price

# Apply discount if total price is over $100
if total_price > 100:
    discount = total_price * 0.10
    total_price -= discount

# Display total price with 2 decimal places
print(f"Total price after discount : ${total_price:.2f}")
