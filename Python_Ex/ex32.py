def add_expense(expenses, amount):
    if isinstance(expenses, list) and isinstance(amount, (int, float)) and amount > 0:
        expenses.append(amount)
        print("Updated Expenses List:")
        print(expenses)
    else:
        print("Invalid input")

expenses = [100, 200, 300]
add_expense(expenses, 150)