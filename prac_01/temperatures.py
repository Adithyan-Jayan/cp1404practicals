"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

print(MENU)
choice = input(">>> ").upper()  # Convert to uppercase for easier comparison

while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32  # Conversion formula
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)  # Conversion formula
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")

    # Display the menu again and get the next choice
    print(MENU)
    choice = input(">>> ").upper()

print("Thank you.")
