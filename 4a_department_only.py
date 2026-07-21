import csv


EMPLOYEE_DEPARTMENTS = {}


with open("employees_list.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        EMPLOYEE_DEPARTMENTS[row["Name"].strip().lower()] = row["Department"].strip()


def verify_department(name, department):
    """
    Checks whether the entered department matches the employee's department.
    """
    employee_name = name.strip().lower()
    entered_department = department.strip().lower()

    if employee_name not in EMPLOYEE_DEPARTMENTS:
        return False

    return EMPLOYEE_DEPARTMENTS[employee_name].lower() == entered_department


def get_verified_department(name):
    """
    Continues asking until the correct department for the employee is entered.
    """
    while True:
        department = input("What department do you work in? ").strip()

        if verify_department(name, department):
            print("Confirmed!")
            return department

        print("Incorrect department, please try again.")


def run(name):
    """
    Receives the employee name from the previous script.
    Only asks for and verifies the department.
    """
    department = get_verified_department(name)
    return department