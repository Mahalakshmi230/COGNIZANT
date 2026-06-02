# COGNIZANT
## Python 3 Programming Exercises
This repository contains solutions for 55 Python Programming Exercises covering fundamentals, data structures, object-oriented programming, file handling, error handling, modules, and real-world application simulations.

The exercises are designed to strengthen problem-solving skills and practical Python development.


## EX:01:Simple Hello World 
## code:
```
print("Hello World!")
```
## output:
<img width="939" height="249" alt="image" src="https://github.com/user-attachments/assets/de16ccbe-88c0-42c5-9851-9e33b7cf56b7" />


## EX:02: Jupyter Notebook
## code:
```
print("Hello from Jupyter Notebook")
```
## output:
<img width="940" height="259" alt="image" src="https://github.com/user-attachments/assets/6f3a3e88-5daa-4f04-a95e-769b93d8098a" />


## EX:03: VS Code Setup
## code:
```
name = "Python"
print(f"VS Code is configured for {name}")
```
## output:
<img width="940" height="96" alt="image" src="https://github.com/user-attachments/assets/25f50f2a-96cf-4a1d-9cb1-ffb2f60142f2" />


## EX:04: Float Precision
## code:
```

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
```
## output:
<img width="935" height="91" alt="image" src="https://github.com/user-attachments/assets/f114295f-b788-435d-85b7-856541e566f7" />


## EX:05: Multiple Assignment 
## code:
```
def display_coordinates(coords):
    x, y = coords  # Multiple assignment

    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        print(f"Coordinates: ({x}, {y})")
    else:
        print("Invalid coordinates")

# Input coordinates
coordinates = (10, 20)

display_coordinates(coordinates)
```
## output:



## EX:06: Modulo Operator
## code:
```
def check_even_odd(number):
    if isinstance(number, int):
        remainder = number % 2

        if remainder == 0:
            print("Even")
        else:
            print("Odd")
    else:
        print("Invalid number")

number = 17

check_even_odd(number)
```
## output:
<img width="940" height="229" alt="image" src="https://github.com/user-attachments/assets/cd0d5fc6-95b0-4039-9a5f-af4e1c35677b" />


## EX:07: Floor Division  
## code:
```
def split_bill(total_bill, people):
    if isinstance(total_bill, (int, float)) and isinstance(people, int) and people > 0:
        share = total_bill // people  # Floor division
        print(f"Individual Share: {share}")
    else:
        print("Invalid input")

total_bill = 1250
people = 4

split_bill(total_bill, people)
```
## output:
<img width="940" height="202" alt="image" src="https://github.com/user-attachments/assets/4060f09b-3010-43b5-b4e8-9e083211e3ff" />


## EX:08: Min/Max Functions  
## code:
```
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
```
## output:
<img width="940" height="217" alt="image" src="https://github.com/user-attachments/assets/e0ba404f-144a-494d-bad7-66b48d2724b1" />


## EX:09: Basic Input  
## code:
```
def greet_user():
    name = input("Enter your name: ")

    if name.strip() == "":
        print("Invalid input")
    else:
        print(f"Hello, {name}! Welcome.")

greet_user()
```
## output:
<img width="940" height="196" alt="image" src="https://github.com/user-attachments/assets/987afd00-d87c-40de-8863-1e9df1a12802" />

## EX:10: Numeric Input 
## code:
```
def next_year_age():
    age_input = input("Enter your age: ")

    if age_input.isdigit():
        age = int(age_input)
        print(f"Next year you'll be {age + 1}")
    else:
        print("Invalid input")

next_year_age()
```
## output:
<img width="940" height="214" alt="image" src="https://github.com/user-attachments/assets/c66fad8d-f52c-4523-b3e1-a7fe2bfa40a6" />


## EX:11: Float Input 
## code:
```
def convert_weight():
    kg_input = input("Enter weight in kilograms: ")

    try:
        kg = float(kg_input)

        if kg >= 0:
            lbs = kg * 2.20462
            print(f"Weight in pounds: {lbs:.2f}")
        else:
            print("Invalid input")
    except ValueError:
        print("Invalid input")

convert_weight()
```
## output:
<img width="940" height="242" alt="image" src="https://github.com/user-attachments/assets/567e705c-eb9f-4920-9200-6f1a4d1fcab5" />


## EX:12: Simple If
## code:
```
def check_pass_fail(marks):
    if isinstance(marks, (int, float)) and 0 <= marks <= 100:
        if marks >= 40:
            print("Pass")
        else:
            print("Fail")
    else:
        print("Invalid marks")

marks = 75

check_pass_fail(marks)
```
## output:
<img width="940" height="228" alt="image" src="https://github.com/user-attachments/assets/f78a48b8-ea75-4251-a12a-260bafb7dd51" />

## EX:13: If-Else
## code:
```
def check_even_odd(num):
    if isinstance(num, int):
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")
    else:
        print("Invalid input")

num = 8

check_even_odd(num)
```
## output:
<img width="940" height="186" alt="image" src="https://github.com/user-attachments/assets/cab48bf1-c9dc-4770-bc3c-fe90948d29f8" />

## EX:14: If-Elif-Else 
## code:
```
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
```
## output:
<img width="940" height="198" alt="image" src="https://github.com/user-attachments/assets/c606cd70-1a2b-4ed3-afd9-75e9b7f4421d" />

## EX:15: Nested If  
## code:
```
def validate_login(user, pwd):
    if user.strip() == "" or pwd.strip() == "":
        print("Invalid input")
    else:
        if user == "admin":
            if pwd == "pass123":
                print("Login Successful")
            else:
                print("Incorrect Password")
        else:
            print("Invalid Username")

user = "admin"
pwd = "pass123"

validate_login(user, pwd)
```
## output:
<img width="940" height="209" alt="image" src="https://github.com/user-attachments/assets/320764ff-6a2a-42ec-906c-1f2d5b46a14b" />

## EX:16: For Loop Basics 
## code:
```
def print_numbers():
    count = 5

    if count > 0:
        for i in range(5):
            print(i + 1)
    else:
        print("Invalid loop count")

print_numbers()
```
## output:
<img width="940" height="203" alt="image" src="https://github.com/user-attachments/assets/62521a98-ed5c-4c4b-bb15-df0c46fc1ed8" />

## EX:17: While Loop
## code:
```
def countdown():
    count = 5

    if count > 0:
        while count > 0:
            print(count)
            count -= 1
    else:
        print("Invalid count value")

countdown()
```
## output:
<img width="940" height="205" alt="image" src="https://github.com/user-attachments/assets/b52e4f33-ac50-4846-a59f-a786f7d2994a" />

## EX:18: Break Statement  
## code:
```
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
```
## output:
<img width="940" height="183" alt="image" src="https://github.com/user-attachments/assets/34a6f370-0bae-474e-a19b-258a26e09908" />

## EX:19: Continue Statement 
## code:
```
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
```
## output:
<img width="940" height="175" alt="image" src="https://github.com/user-attachments/assets/d206525f-461b-458e-9379-d9c9f4daea51" />

## EX:20: Pass Statement 
## code:
```
def placeholder_function():
    pass 

placeholder_function()

print("Function defined")
```
## output:
<img width="940" height="172" alt="image" src="https://github.com/user-attachments/assets/cdfaa230-7d97-4f69-8b3d-dcf9c53ddeba" />


## EX:21: Consistent Indentation 
## code:
```
def check_nested():
    condition1 = True
    condition2 = True

    if condition1:
        if condition2:
            print("Nested")

    print("Confirmation message")

check_nested()
```
## output:


## EX:22: Comment Usage  
## code:
```
def calculate_salary():
    base_salary = 50000
    bonus = 10000
    total_salary = base_salary + bonus
    print(f"Total Salary: {total_salary}")

calculate_salary()
```
## output:
<img width="940" height="177" alt="image" src="https://github.com/user-attachments/assets/cfc0831d-a7ee-4816-9b66-4faae6c7f9e6" />


## EX:23: Import Standard Module  
## code:
```
import math

def calculate_area(radius):
    if radius > 0:
        area = math.pi * radius ** 2
        print(f"Area of Circle: {area:.2f}")
    else:
        print("Invalid radius")

radius = 5

calculate_area(radius)
```
## output:
<img width="940" height="168" alt="image" src="https://github.com/user-attachments/assets/6cee50f6-4646-4c2b-87d6-2aa428789868" />

## EX:24:  All Import  
## code:
```
from math import *

def math_operations(num):
    if num >= 0:
        print(f"Square Root: {sqrt(num):.2f}")
        print(f"Power: {pow(num, 2):.2f}")
        print(f"Value of Pi: {pi:.2f}")
    else:
        print("Invalid input")

num = 16

math_operations(num)
```
## output:
<img width="939" height="171" alt="image" src="https://github.com/user-attachments/assets/9c00b598-7e66-4959-b5a2-929a9a87525c" />

## EX:25: Parameters
## code:
```
def add(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return "Invalid input"

result = add(5, 3)
print(f"Result: {result}")
```
## output:
<img width="939" height="158" alt="image" src="https://github.com/user-attachments/assets/89f24703-ec5b-4400-b9f6-e4f621239d01" />

## EX:26: Multiple Parameters
## code:
```
def area_rectangle(length, width):
    if isinstance(length, (int, float)) and isinstance(width, (int, float)) and length > 0 and width > 0:
        return length * width
    else:
        return "Invalid input"

result = area_rectangle(5, 3)
print(f"Area: {result}")
```
## output:
<img width="939" height="165" alt="image" src="https://github.com/user-attachments/assets/8772488e-872a-4a31-aa9c-063534e945dd" />

## EX:27: Len Function   
## code:
```
def string_length(text):
    if isinstance(text, str) and text.strip() != "":
        length = len(text)
        print(f"Length of string: {length}")
    else:
        print("Invalid input")

text = "Hello World"
string_length(text)
```
## output:
<img width="940" height="159" alt="image" src="https://github.com/user-attachments/assets/72291035-0509-4eaf-811b-243e39292735" />

## EX:28: Write to File 
## code:
```
def write_file():
    file = open("message.txt", "w")
    file.write("Hello World")
    file.close()
    print("File written successfully")

write_file()
```
## output:
<img width="940" height="144" alt="image" src="https://github.com/user-attachments/assets/86ff6a67-0f4d-4559-bb80-608324a93763" />

## EX:29: Read from File 
## code:
```
def read_file():
    try:
        file = open("message.txt", "r")
        content = file.read()
        file.close()
        print("File Content:")
        print(content)
    except FileNotFoundError:
        print("File not found")

read_file()
```
## output:
<img width="940" height="204" alt="image" src="https://github.com/user-attachments/assets/1c8f5075-bd02-4222-93bd-e04192c06d24" />

## EX:30: Basic Try-Except
## code:
```
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(divide(10, 2))
print(divide(10, 0))
```
## output:
<img width="939" height="188" alt="image" src="https://github.com/user-attachments/assets/5a161972-3847-4498-a243-021bad647571" />

## EX:31: Create List 
## code:
```
def show_cart(cart):
    if isinstance(cart, list) and len(cart) > 0:
        print("Shopping Cart Items:")
        for item in cart:
            print(item)
    else:
        print("Invalid cart")

cart = [100, 250, 75]

show_cart(cart)
```
## output:
<img width="939" height="186" alt="image" src="https://github.com/user-attachments/assets/f51c052f-da15-4de5-9bd3-dce25dc018dd" />

## EX:32: Append to List 
## code:
```
def add_expense(expenses, amount):
    if isinstance(expenses, list) and isinstance(amount, (int, float)) and amount > 0:
        expenses.append(amount)
        print("Updated Expenses List:")
        print(expenses)
    else:
        print("Invalid input")

expenses = [100, 200, 300]
add_expense(expenses, 150)
```
## output:
<img width="940" height="179" alt="image" src="https://github.com/user-attachments/assets/3a0bfacf-0d76-4a1c-883f-7b7a062aec25" />

## EX:33: Update Dictionary  
## code:
```
def update_employee():
    emp1 = {"name": "Maha", "id": 101}
    emp2 = {"salary": 50000, "department": "AI"}

    if not emp1 or not emp2:
        return "Invalid input"

    emp1.update(emp2)

    return emp1

print(update_employee())
```
## output:
<img width="940" height="156" alt="image" src="https://github.com/user-attachments/assets/a0c47892-c329-42ea-955f-76fc6c99585b" />

## EX:34: Nested Dictionary 
## code:
```
def get_salary(dept, emp_name):
    employees = {
        "AI": {
            "Maha": 60000,
            "Arun": 55000
        },
        "IT": {
            "Kiran": 70000,
            "Meena": 65000
        }
    }

    if dept not in employees:
        return "Department not found"

    if emp_name not in employees[dept]:
        return "Employee not found"

    return employees[dept][emp_name]

print(get_salary("AI", "Roshini"))
```
## output:
<img width="939" height="184" alt="image" src="https://github.com/user-attachments/assets/b04c252e-1701-4dd2-9202-5c9790eddf3b" />


## EX:35: Create Tuple 
## code:
```
def show_coordinates():
    coordinates = (10, 20)

    if len(coordinates) != 2:
        return "Invalid coordinates"

    x, y = coordinates

    return f"X: {x}, Y: {y}"

print(show_coordinates())
```
## output:
<img width="940" height="163" alt="image" src="https://github.com/user-attachments/assets/50138778-3a55-4f39-bdce-c52835b68ffb" />


## EX:36: Set Intersection 
## code:
```
def common_skills():
    set1 = {"Python", "Java", "SQL", "AI"}
    set2 = {"Python", "C++", "SQL", "ML"}

    if not set1 or not set2:
        return "Invalid input"

    return set1 & set2   

print("Common Skills:", common_skills())
```
## output:
<img width="939" height="173" alt="image" src="https://github.com/user-attachments/assets/a491473f-1b8d-4ca1-8f11-55594ac5b48d" />

## EX:37: Multiple Instances
## code:
```
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        return f"Name: {self.name}, ID: {self.emp_id}"


def main():
    emp1 = Employee("Roshini", 101)
    emp2 = Employee("Arun", 102)
    emp3 = Employee("Meena", 103)

    employees = [emp1, emp2, emp3]

    for emp in employees:
        print(emp.display())


main()
```
## output:
<img width="940" height="204" alt="image" src="https://github.com/user-attachments/assets/be9e0746-fa5a-42c4-95bd-559feddc7f21" />

## EX:38: Method Chaining
## code:
```
class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def set_salary(self, salary):
        if salary <= 0:
            self.salary = 0
        else:
            self.salary = salary
        return self

    def apply_raise(self, percent):
        if percent < 0:
            percent = 0
        self.salary += self.salary * (percent / 100)
        return self

    def display(self):
        print("Employee:", self.name)
        print("Final Salary:", self.salary)
        return self


def main():
    emp = Employee("Maha")
    emp.set_salary(50000).apply_raise(10).display()


main()
```
## output:
<img width="939" height="185" alt="image" src="https://github.com/user-attachments/assets/40494409-d217-4a8f-a438-5c6b3d8ebc23" />

## EX: 39:  Polymorphism
## code:
```
class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer writes code")


class Tester(Employee):
    def work(self):
        print("Tester tests the application")


def main():
    employees = [Developer(), Tester(), Employee()]

    for emp in employees:
        emp.work()


main()
```
## output:
<img width="940" height="180" alt="image" src="https://github.com/user-attachments/assets/ad37a2d5-a57a-47d2-9839-0978fac45e6f" />

## EX:40: Class Methods 
## code:
```
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    @classmethod
    def from_string(cls, data):
        name, salary = data.split(",")

        if not salary.isdigit():
            return "Invalid salary"

        return cls(name, int(salary))


def main():
    emp = Employee.from_string("Shubh,75000")
    print(emp.display())


main()
```
## output:
<img width="939" height="188" alt="image" src="https://github.com/user-attachments/assets/2cb06af0-a23b-4dc8-8754-ecdc15906ea1" />

## EX:41: Employee Management System 
## code:
```
# OOP + File Handling + JSON)
import json

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def to_dict(self):
        return {
            "id": self.emp_id,
            "name": self.name,
            "salary": self.salary
        }


def save_employees(emp_list):
    data = {}

    for emp in emp_list:
        data[emp.emp_id] = emp.to_dict()

    with open("emps.json", "w") as file:
        json.dump(data, file)

    return "Data saved successfully"


def load_employees():
    try:
        with open("emps.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return "No file found"


def main():
    e1 = Employee(101, "Maha", 60000)
    e2 = Employee(102, "Arun", 55000)

    employees = [e1, e2]

    print(save_employees(employees))
    print(load_employees())


main()
```
## output:
<img width="940" height="218" alt="image" src="https://github.com/user-attachments/assets/55ea6df5-4ede-4090-a435-e31a732d11a6" />

## EX:42: Data Analysis Pipeline 
## code:
```
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
```
## output:
<img width="940" height="170" alt="image" src="https://github.com/user-attachments/assets/e996e44e-73db-47dd-8445-ed16ea250952" />

## EX:43: Configuration Manager
## code:
```
import configparser

class Config:
    def __init__(self, file_name):
        self.file_name = file_name
        self.config = configparser.ConfigParser()

    def load(self):
        self.config.read(self.file_name)
        return self.config


class DatabaseConfig(Config):
    def get_db_settings(self):
        config = self.load()

        if "database" not in config:
            return "Database section missing"

        db = config["database"]

        required_keys = ["host", "user", "password"]

        for key in required_keys:
            if key not in db:
                return f"Missing key: {key}"

        return {
            "host": db["host"],
            "user": db["user"],
            "password": db["password"]
        }


def main():
    obj = DatabaseConfig("db.ini")
    print(obj.get_db_settings())


main()
```
## output:
<img width="939" height="171" alt="image" src="https://github.com/user-attachments/assets/fd5bc53d-5189-4ea5-aceb-826491d16fe5" />

## EX:44: CSV Data Processor
## code:
```
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
```
## output:
<img width="939" height="189" alt="image" src="https://github.com/user-attachments/assets/3b64806c-a753-4147-91ea-d425559d9658" />

## EX:45: Expense Tracker 
## code:
```
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
```
## output:
<img width="939" height="179" alt="image" src="https://github.com/user-attachments/assets/4c7b62d1-ae07-4cdc-ad03-6c11f25e0652" />

## EX:46: API Response Handler 
## code:
```
import requests

def get_weather(city):
    try:
        if city.strip() == "":
            return "Invalid city name"

        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(url)

        if response.status_code != 200:
            return "Error fetching data"

        data = response.json()

        current = data["current_condition"][0]

        temp = current["temp_C"]
        weather = current["weatherDesc"][0]["value"]

        return f"Temperature: {temp}°C, Condition: {weather}"

    except requests.exceptions.RequestException:
        return "Network error"


print(get_weather("Chennai"))
```
## output:
<img width="939" height="193" alt="image" src="https://github.com/user-attachments/assets/e02eaaae-44fa-43cf-a7af-cba2cc892904" />

## EX:47: Complete Calculator Program
## code:
```
def calculate(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            return "Invalid operator"

    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid input type"


def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /): ")

        result = calculate(a, b, op)

        print("Result:", result)

    except ValueError:
        print("Invalid number input")


main()
```
## output:
<img width="939" height="280" alt="image" src="https://github.com/user-attachments/assets/b1ccbee6-16b7-4740-bd90-70c8f53e6524" />

## EX:48: Shopping Cart System
## code:
```
class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        self.items = [item for item in self.items if item.name != name]

    def calculate_total(self):
        total = sum(item.total_price() for item in self.items)
        gst = total * 0.18
        final_total = total + gst
        return total, gst, final_total

    def print_receipt(self):
        print("\n--- Receipt ---")
        for item in self.items:
            print(item.name, "-", item.quantity, "x", item.price, "=", item.total_price())

        total, gst, final_total = self.calculate_total()

        print("\nTotal:", total)
        print("GST (18%):", gst)
        print("Final Total:", final_total)


def main():
    cart = ShoppingCart()

    cart.add_item(CartItem("Rice", 50, 2))
    cart.add_item(CartItem("Milk", 30, 3))
    cart.add_item(CartItem("Soap", 40, 1))

    cart.remove_item("Soap")

    cart.print_receipt()


main()
```
## output:
<img width="940" height="254" alt="image" src="https://github.com/user-attachments/assets/3eeaec8b-3d14-44b7-8d3f-d1027ee874ab" />

## EX:49: Temperature Converter GUI 
## code:
```
class TemperatureConverter:

    def c_to_f(self, c):
        return (c * 9/5) + 32

    def f_to_c(self, f):
        return (f - 32) * 5/9

    def c_to_k(self, c):
        return c + 273.15

    def k_to_c(self, k):
        return k - 273.15


def main():
    converter = TemperatureConverter()

    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Enter choice (1-4): ")

    try:
        temp = float(input("Enter temperature: "))

        if choice == "1":
            print("Result:", round(converter.c_to_f(temp), 2))

        elif choice == "2":
            print("Result:", round(converter.f_to_c(temp), 2))

        elif choice == "3":
            print("Result:", round(converter.c_to_k(temp), 2))

        elif choice == "4":
            print("Result:", round(converter.k_to_c(temp), 2))

        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid temperature input")


main()
```
## output:


## EX:50: Backup Utility 
## code:
```
import shutil
import os

def backup_files():
    source_folder = "source_files"
    backup_folder = "backup_files"
    log_file = "backup.log"

    os.makedirs(backup_folder, exist_ok=True)

    copied_files = set()

    with open(log_file, "a") as log:
        for file_name in os.listdir(source_folder):

            source_path = os.path.join(source_folder, file_name)
            backup_path = os.path.join(backup_folder, file_name)

            if file_name in copied_files:
                continue

            try:
                shutil.copy(source_path, backup_path)
                copied_files.add(file_name)
                log.write(f"Copied: {file_name}\n")

            except FileNotFoundError:
                log.write(f"Missing file: {file_name}\n")

    return "Backup completed successfully"


print(backup_files())
```
## output:
<img width="940" height="114" alt="image" src="https://github.com/user-attachments/assets/10b1fc0a-631b-464b-81ea-30c5ac3e359d" />

## EX:51: URL Shortener 
## code:
```
import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def _generate_short_code(self, url):
        # Create hash and take first 6 characters
        hash_object = hashlib.md5(url.encode())
        return hash_object.hexdigest()[:6]

    def shorten_url(self, url):
        if not url:
            return "Invalid URL"

        short_code = self._generate_short_code(url)
        self.url_map[short_code] = url

        return short_code

    def get_original_url(self, short_code):
        return self.url_map.get(short_code, "URL not found")


def main():
    shortener = URLShortener()

    url = "https://www.google.com"
    short_code = shortener.shorten_url(url)

    print("Short URL code:", short_code)
    print("Original URL:", shortener.get_original_url(short_code))


main()
```
## output:
<img width="939" height="166" alt="image" src="https://github.com/user-attachments/assets/da34186e-aca8-49e0-a9e3-8f7e5c65b2fa" />

## EX:52: Gradebook System 
## code:
```
import json

# Student data structure:
# student_name -> list of grades

def calculate_gpa(grades):
    if not grades:
        return 0

    return sum(grades) / len(grades)


def add_student_grade(data, name, grade):
    if name not in data:
        data[name] = []

    if 0 <= grade <= 100:
        data[name].append(grade)
    else:
        print("Invalid grade ignored")


def class_average(data):
    all_grades = []

    for grades in data.values():
        all_grades.extend(grades)

    if not all_grades:
        return 0

    return sum(all_grades) / len(all_grades)


def save_data(data, filename="grades.json"):
    with open(filename, "w") as file:
        json.dump(data, file)


def load_data(filename="grades.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def main():
    students = load_data()

    add_student_grade(students, "Roshini", 85)
    add_student_grade(students, "Arun", 90)
    add_student_grade(students, "Roshini", 78)

    print("GPA Roshini:", calculate_gpa(students["Roshini"]))
    print("Class Average:", class_average(students))

    save_data(students)


main()
```
## output:
<img width="939" height="164" alt="image" src="https://github.com/user-attachments/assets/15220342-3a21-4220-8d6d-3fa9bea13d21" />

## EX:53: Task Scheduler
## code:
```
from datetime import datetime

class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority

    def is_overdue(self):
        return self.due_date < datetime.now()


class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_sorted_tasks(self):
        return sorted(self.tasks, key=lambda t: t.due_date)

    def get_overdue_tasks(self):
        return [t for t in self.tasks if t.is_overdue()]

    def display_tasks(self):
        print("\n--- Task List ---")
        for task in self.get_sorted_tasks():
            status = "Overdue" if task.is_overdue() else "Pending"
            print(task.name, "-", task.due_date.date(), "-", task.priority, "-", status)


def main():
    scheduler = TaskScheduler()

    scheduler.add_task(Task("Finish Project", "2026-05-20", "High"))
    scheduler.add_task(Task("Study SQL", "2026-06-05", "Medium"))
    scheduler.add_task(Task("Practice Python", "2026-05-10", "High"))

    scheduler.display_tasks()

    print("\nOverdue Tasks:")
    for task in scheduler.get_overdue_tasks():
        print(task.name)


main()
```
## output:
<img width="939" height="230" alt="image" src="https://github.com/user-attachments/assets/95998538-42cb-4cf5-b8d3-ae4abcf8a9d1" />

## EX:54: Inventory Manager
## code:
```
#(OOP + Inheritance + Dictionaries + Sets)
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        return f"{self.name} | Price: {self.price} | Stock: {self.stock}"


class Perishable(Product):
    def __init__(self, name, price, stock, expiry_date):
        super().__init__(name, price, stock)
        self.expiry_date = expiry_date


class Electronics(Product):
    def __init__(self, name, price, stock, warranty_years):
        super().__init__(name, price, stock)
        self.warranty_years = warranty_years


class InventoryManager:
    def __init__(self):
        self.products = {}
        self.low_stock_alert = set()

    def add_product(self, product):
        self.products[product.name] = product

        if product.stock < 5:
            self.low_stock_alert.add(product.name)

    def update_stock(self, name, new_stock):
        if name in self.products:
            self.products[name].stock = new_stock

            if new_stock < 5:
                self.low_stock_alert.add(name)
            elif name in self.low_stock_alert:
                self.low_stock_alert.remove(name)

    def show_inventory(self):
        print("\n--- Inventory ---")
        for product in self.products.values():
            print(product.display())

    def show_low_stock(self):
        print("\n--- Low Stock Items ---")
        for item in self.low_stock_alert:
            print(item)


def main():
    manager = InventoryManager()

    p1 = Perishable("Milk", 50, 3, "2026-06-10")
    p2 = Electronics("Phone", 15000, 10, 2)
    p3 = Product("Book", 200, 2)

    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)

    manager.show_inventory()
    manager.show_low_stock()

    manager.update_stock("Phone", 3)

    print("\nAfter Update:")
    manager.show_inventory()
    manager.show_low_stock()


main()
```
## output:
<img width="940" height="251" alt="image" src="https://github.com/user-attachments/assets/eb45654c-7d3f-4704-b0d7-8f3bd9737bce" />

## EX:55: Budget Planner 
## code:
```
import matplotlib.pyplot as plt

class Category:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0

    def add_expense(self, amount):
        if amount <= 0:
            return "Invalid amount"
        self.spent += amount

    def status(self):
        if self.spent > self.limit:
            return f"{self.name}: Budget exceeded!"
        return f"{self.name}: Within budget"


class BudgetPlanner:
    def __init__(self):
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def show_status(self):
        print("\n--- Budget Status ---")
        for c in self.categories:
            print(c.status())

    def show_chart(self):
        names = [c.name for c in self.categories]
        spent = [c.spent for c in self.categories]

        plt.pie(spent, labels=names, autopct="%1.1f%%")
        plt.title("Monthly Budget Distribution")
        plt.show()


def main():
    planner = BudgetPlanner()

    food = Category("Food", 5000)
    travel = Category("Travel", 3000)
    shopping = Category("Shopping", 4000)

    food.add_expense(4500)
    travel.add_expense(3500)
    shopping.add_expense(2000)

    planner.add_category(food)
    planner.add_category(travel)
    planner.add_category(shopping)

    planner.show_status()
    planner.show_chart()


main()
```
## output:

<img width="940" height="251" alt="image" src="https://github.com/user-attachments/assets/93c35956-3145-4855-aae8-1d0774857dc8" />


<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/1b76eadb-b450-4351-a139-cb001e97927e" />


## Technologies Used
Python 3
Jupyter Notebook
VS Code
JSON
CSV
Requests
Statistics
ConfigParser
Datetime
Math Module
Matplotlib
OOP Concepts

## Author
Mahalakshmi R

B.TECH. Artificial Intelligence and Data Science Saveetha Engineering College


































