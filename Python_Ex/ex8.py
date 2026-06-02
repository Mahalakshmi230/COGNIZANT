def find_salary_range(salaries):
    if isinstance(salaries, list) and len(salaries) > 0:
        lowest_salary = min(salaries)
        highest_salary = max(salaries)

        print(f"Lowest Salary: {lowest_salary}")
        print(f"Highest Salary: {highest_salary}")
    else:
        print("Invalid salary list")


salaries = [50000, 75000, 62000, 95000]

find_salary_range(salaries)