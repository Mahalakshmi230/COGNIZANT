def check_even_odd(num):
    if isinstance(num, int):
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")
    else:
        print("Invalid input")

num = 811

check_even_odd(num)