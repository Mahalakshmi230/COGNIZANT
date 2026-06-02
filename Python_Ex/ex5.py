def display_coordinates(coords):
    x, y = coords  # Multiple assignment

    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        print(f"Coordinates: ({x}, {y})")
    else:
        print("Invalid coordinates")

# Input coordinates
coordinates = (10, 20)

display_coordinates(coordinates)