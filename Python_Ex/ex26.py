def area_rectangle(length, width):
    if isinstance(length, (int, float)) and isinstance(width, (int, float)) and length > 0 and width > 0:
        return length * width
    else:
        return "Invalid input"

result = area_rectangle(5, 3)
print(f"Area: {result}")