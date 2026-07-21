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


def load_name_from_checkin_data():
    """Read the employee name that was already saved by the earlier script.
    Expected format of checkin_data.txt: NAME,DAYS  (example: STACY,203)"""
    with open("checkin_data.txt", "r") as file:
        first_line = file.readline().strip()
        name = first_line.split(",")[0]
        return name


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
    name = load_name_from_checkin_data()

    department = input("What department are you in? ").strip()

    if not verify_department(name, department, employee_departments):
        print(f"Error: '{department}' is not the correct department for {name}.")
        return  # stop here, no retry loop

    save_department(name, department)
    print("Department verified and saved.")


if __name__ == "__main__":
    run()