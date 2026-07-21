import csv


VALID_DEPARTMENTS = []


with open("employees_list.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        VALID_DEPARTMENTS.append(row["Department"].strip())


def verify_department(department):
    return department.strip().lower() in [
        dept.lower() for dept in VALID_DEPARTMENTS
    ]


def save_department(department):
    with open("department_report.txt", "w") as file:
        file.write("Department Verification Report\n")
        file.write("-----------------------------\n")
        file.write(f"Department: {department}\n")


def run():

    while True:
        department = input("What department are you in? ").strip()

        if verify_department(department):
            break

        print("Incorrect department, please try again.")

    save_department(department)


if __name__ == "__main__":
    run()