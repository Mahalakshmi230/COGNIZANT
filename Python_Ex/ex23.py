import math

def calculate_area(radius):
    if radius > 0:
        area = math.pi * radius ** 2
        print(f"Area of Circle: {area:.2f}")
    else:
        print("Invalid radius")

radius = 5

calculate_area(radius)