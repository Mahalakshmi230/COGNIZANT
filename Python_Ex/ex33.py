def update_employee():
    emp1 = {"name": "Maha", "id": 101}
    emp2 = {"salary": 50000, "department": "AI"}

    if not emp1 or not emp2:
        return "Invalid input"

    emp1.update(emp2)

    return emp1

print(update_employee())