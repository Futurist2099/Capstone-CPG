import csv


VALID_DEPARTMENTS = []


with open("employees_list.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        VALID_DEPARTMENTS.append(row["Department"].strip())


def verify_department(department):
    """
    Return True if the department exists in employees_list.csv.
    """
    return department.strip().lower() in [
        dept.lower() for dept in VALID_DEPARTMENTS
    ]


def get_verified_department():
    """
    Keep asking for a department until a valid department is entered.
    """
    while True:
        department = input("What department are you in? ").strip()

        if verify_department(department):
            return department

        print("Incorrect department, please try again.")


def run():
    """
    Main function to verify department.
    """
    department = get_verified_department()

    print(f"Department: {department}")

    return department


if __name__ == "__main__":
    run()