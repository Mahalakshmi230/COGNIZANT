def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(divide(10, 2))
print(divide(10, 0))