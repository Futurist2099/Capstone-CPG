employee_file = "employee.txt"

name = input("Enter your name: ")

with open(employee_file, "r") as file:
    employees = file.read().splitlines()

if name in employees:
    print("Employee verified.")
else:
    print("Employee not found.")