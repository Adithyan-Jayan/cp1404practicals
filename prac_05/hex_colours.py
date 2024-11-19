"""
CP1404/CP5632 Practical
Dictionary of color names and their hex codes
"""
COLOUR_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "ashgrey": "#b2beb5",
    "azure4": "#838b8b",
    "aquamarine": "#7fffd4",
    "coral1": "#ff7256",
    "falured": "#801818",
    "bisque": "#ffe4c4",
    "frenchpink": "#fd6c9e",
    "blanchedalmond": "#ffebcd",
    "keylime": "#e8f48c"
}


def main():
    # Display all colors
    for colour, hex_code in COLOUR_TO_HEX.items():
        print(f"{colour.title():<15} is {hex_code}")

    while True:
        color_name = input("Enter color name: ").strip().lower()  # Convert input to lowercase
        if color_name == "":
            break

        # Look up the color code in the dictionary
        if color_name in COLOUR_TO_HEX:
            print(f"The code for {color_name.title()} is {COLOUR_TO_HEX[color_name]}")
        else:
            print("Invalid color name")


if __name__ == "__main__":
    main()
