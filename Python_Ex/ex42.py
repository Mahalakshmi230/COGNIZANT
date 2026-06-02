import statistics

def read_sales():
    try:
        with open("sales.txt", "r") as file:
            data = file.readlines()

        sales = []

        for value in data:
            value = value.strip()

            if value.isdigit():
                sales.append(int(value))

        if len(sales) == 0:
            return "No valid data"

        mean_val = statistics.mean(sales)
        median_val = statistics.median(sales)

        return f"Mean: {mean_val}, Median: {median_val}"

    except FileNotFoundError:
        return "File not found"


print(read_sales())