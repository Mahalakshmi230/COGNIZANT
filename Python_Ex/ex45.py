import csv
from datetime import datetime

def expense_tracker():
    try:
        expenses = []

        current_month = datetime.now().month
        current_year = datetime.now().year

        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                date = datetime.strptime(row["date"], "%Y-%m-%d")
                amount = float(row["amount"])
                category = row["category"]

                # Filter current month
                if date.month == current_month and date.year == current_year:
                    expenses.append({
                        "date": date,
                        "amount": amount,
                        "category": category
                    })

        if not expenses:
            return "No expenses for current month"

        # Group by category
        summary = {}

        for exp in expenses:
            cat = exp["category"]
            summary[cat] = summary.get(cat, 0) + exp["amount"]

        return summary

    except FileNotFoundError:
        return "File not found"


print(expense_tracker())