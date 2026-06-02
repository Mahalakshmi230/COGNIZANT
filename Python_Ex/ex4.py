
def calculate_net_salary(salary, tax_rate):
    if salary <= 0:
        return "Invalid salary"

    if tax_rate < 0 or tax_rate > 1:
        return "Invalid tax rate"

    tax = salary * tax_rate
    net_salary = salary - tax

    return net_salary


salary = 75000.5
tax_rate = 0.18

net_salary = calculate_net_salary(salary, tax_rate)

if isinstance(net_salary, str):
    print(net_salary)
else:
    print(f"Net Salary: {net_salary:.2f}")