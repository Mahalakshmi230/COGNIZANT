def sum_odd_numbers():
    total = 0
    limit = 10

    if limit > 0:
        for i in range(10):
            if i % 2 == 0:
                continue
            total += i

        print(f"Sum of odd numbers: {total}")
    else:
        print("Invalid range")

sum_odd_numbers()