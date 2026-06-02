import csv

def process_csv():
    try:
        employees = []

        with open("employees.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                row["salary"] = int(row["salary"])
                employees.append(row)

        if len(employees) == 0:
            return "No data found"

        high_salary = [emp for emp in employees if emp["salary"] > 50000]

        total_salary = sum(emp["salary"] for emp in employees)
        avg_salary = total_salary / len(employees)

        return {
            "high_salary_employees": high_salary,
            "average_salary": avg_salary
        }

    except FileNotFoundError:
        return "File not found"


print(process_csv())