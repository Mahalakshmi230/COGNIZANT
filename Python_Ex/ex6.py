def check_even_odd(number):
    if isinstance(number, int):
        remainder = number % 2

        if remainder == 0:
            print("Even")
        else:
            print("Odd")
    else:
        print("Invalid number")

number = 17

check_even_odd(number)