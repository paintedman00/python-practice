def get_color_input():
    while True:
        color = input("Enter a color (red, green, blue, yellow, cyan, magenta, white, black): ").lower()
        if color in ["red", "green", "blue", "yellow", "cyan", "magenta", "white", "black"]:
            return color
        else:
            print("Invalid color. Please choose from the list.")

def mix_colors(color1, color2):
    if color1 == color2:
        return color1
    elif (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
        return "magenta"
    elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
        return "orange"
    elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
        return "green"
    elif (color1 in ["red", "blue", "yellow"] and color2 == "white") or (color2 in ["red", "blue", "yellow"] and color1 == "white"):
        return color1 if color1 != "white" else color2
    elif (color1 == "black" or color2 == "black"):
        return "black"
    elif (color1 == "cyan" and color2 == "magenta") or (color1 == "magenta" and color2 == "cyan"):
        return "blue"
    elif (color1 == "cyan" and color2 == "yellow") or (color1 == "yellow" and color2 == "cyan"):
        return "green"
    elif (color1 == "magenta" and color2 == "yellow") or (color1 == "yellow" and color2 == "magenta"):
        return "red"
    elif (color1 == "cyan" and color2 == "red") or (color1 == "red" and color2 == "cyan"):
        return "magenta"
    else:
        return "unknown"

if __name__ == "__main__":
    print("Simple Color Mixer")

    color1 = get_color_input()
    color2 = get_color_input()

    mixed_color = mix_colors(color1, color2)

    if mixed_color == "unknown":
        print("Cannot mix these colors.")
    else:
        print(f"Mixed color: {mixed_color}")
