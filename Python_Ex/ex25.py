def add(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return "Invalid input"

result = add(5, 3)
print(f"Result: {result}")