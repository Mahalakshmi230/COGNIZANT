def greet_user():
    name = input("Enter your name: ")

    if name.strip() == "":
        print("Invalid input")
    else:
        print(f"Hello, {name}! Welcome.")

greet_user()