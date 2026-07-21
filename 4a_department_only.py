import csv


def load_employee_departments():
    """Build a lookup: {employee_name (lowercase): department}"""
    employee_departments = {}
    with open("employees_list.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row["Name"].strip().lower()
            department = row["Department"].strip()
            employee_departments[name] = department
    return employee_departments


def verify_department(name, department, employee_departments):
    name_key = name.strip().lower()
    if name_key not in employee_departments:
        return False  # employee not found at all
    actual_department = employee_departments[name_key]
    return department.strip().lower() == actual_department.lower()


def save_department(name, department):
    with open("department_report.txt", "w") as file:
        file.write("Department Verification Report\n")
        file.write("-----------------------------\n")
        file.write(f"Name: {name}\n")
        file.write(f"Department: {department}\n")


def run():
    employee_departments = load_employee_departments()
    name = input("What is your name? ").strip()
    while True:
        department = input("What department are you in? ").strip()
        if verify_department(name, department, employee_departments):
            break
        print("Incorrect department, please try again.")
    save_department(name, department)

