def convert_weight():
    kg_input = input("Enter weight in kilograms: ")

    try:
        kg = float(kg_input)

        if kg >= 0:
            lbs = kg * 2.20462
            print(f"Weight in pounds: {lbs:.2f}")
        else:
            print("Invalid input")
    except ValueError:
        print("Invalid input")

convert_weight()