import csv


VALID_DEPARTMENTS = []


with open("employees_list.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        VALID_DEPARTMENTS.append(row["Department"])


def verify_department(department):
    return department.strip().lower() in [
        dept.lower() for dept in VALID_DEPARTMENTS
    ]


def save_department(department):
    with open("checkin_data.txt", "w") as file:
        file.write("Employee Check-In Report\n")
        file.write("-------------------------\n")
        file.write(f"Department: {department}\n")


def run():

    department = input("What department are you in? ").strip()

    if not verify_department(department):
        print(f"\nERROR: '{department}' is not a valid department.")
        return

    save_department(department)

    print("\nVerification successful!")
    print(f"Department: {department}")


if __name__ == "__main__":
    run()