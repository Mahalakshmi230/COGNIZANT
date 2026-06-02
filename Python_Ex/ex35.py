def show_coordinates():
    coordinates = (10, 20)

    if len(coordinates) != 2:
        return "Invalid coordinates"

    x, y = coordinates

    return f"X: {x}, Y: {y}"

print(show_coordinates())