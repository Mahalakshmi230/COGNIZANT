def find_first_even(limit):
    if isinstance(limit, int) and limit > 0:
        for i in range(1, limit + 1):
            if i % 2 == 0:
                print(f"First even number: {i}")
                break
    else:
        print("Invalid range size")

limit = 10

find_first_even(limit)