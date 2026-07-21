import csv


EMPLOYEES = {}


with open("employees_list.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        EMPLOYEES[row["Name"].strip().lower()] = row["Department"].strip()


def verify_employee_department(name, department):
    """
    Returns True if the employee exists and the department matches.
    """
    employee_name = name.strip().lower()
    department = department.strip().lower()

    if employee_name not in EMPLOYEES:
        return False

    return EMPLOYEES[employee_name].lower() == department


def save_department(name, department):
    # Save the department report to its own file so we don't
    # overwrite the shared check-in data used by other scripts.
    with open("department_report.txt", "w") as file:
        file.write("Employee Check-In Report\n")
        file.write("-------------------------\n")
        file.write(f"Employee: {name}\n")
        file.write(f"Department: {department}\n")


def run():
    name = input("What is your name? ").strip()

    while True:
        department = input("What department are you in? ").strip()

        if verify_employee_department(name, department):
            break

        print("Incorrect department, please try again.")

    save_department(name, department)

    print("\nVerification successful!")
    print(f"Employee: {name}")
    print(f"Department: {department}")
    print("Department report saved to department_report.txt")


if __name__ == "__main__":
    run()