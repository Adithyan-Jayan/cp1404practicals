"""
CP1404/CP5632 - Practical
Sales bonus

"""
#  Get sales
sales = float(input("Enter sales: $"))
while sales > 0:
    # Calculating bonus based on sales amount
    if sales < 1000:
        bonus = sales * 0.10  # 10% bonus for sales under $1000
    else:
        bonus = sales * 0.15  # 15% bonus for sales $1000 or over
    print(f"The bonus for ${sales:.2f} sales is: ${bonus:.2f}")
    sales = float(input("Enter sales: $"))
print("Invalid sales amount")

