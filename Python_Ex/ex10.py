def next_year_age():
    age_input = input("Enter your age: ")

    if age_input.isdigit():
        age = int(age_input)
        print(f"Next year you'll be {age + 1}")
    else:
        print("Invalid input")

next_year_age()