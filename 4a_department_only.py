import csv


VALID_DEPARTMENTS = []


with open("employees_list.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        VALID_DEPARTMENTS.append(row["Department"].strip())


def verify_department(department):
    """
    Checks if the entered department exists in employees_list.csv.
    """
    return department.strip().lower() in [
        dept.lower() for dept in VALID_DEPARTMENTS
    ]


def get_verified_department():
    """
    Continues asking until a correct department is entered.
    """
    while True:
        department = input("What department do you work in? ").strip()

        if verify_department(department):
            print("Confirmed!")
            return department

        print("Incorrect department, please try again.")


def run():
    get_verified_department()


if __name__ == "__main__":
    run()