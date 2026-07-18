import csv
import user_input


# Lists of valid names and departments
VALID_NAMES = []
VALID_DEPARTMENTS = []


# Read employee information from the CSV file
with open("employees_list.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        VALID_NAMES.append(row["Name"])
        VALID_DEPARTMENTS.append(row["Department"])


def verify_name(name):
    """
    Checks if the entered name exists
    in employees_list.csv.
    """
    return name.strip().lower() in [
        employee.lower() for employee in VALID_NAMES
    ]


def verify_department(department):
    """
    Checks if the entered department exists
    in employees_list.csv.
    """
    return department.strip().lower() in [
        dept.lower() for dept in VALID_DEPARTMENTS
    ]


def determine_status(days):
    """
    Determines employee status.
    """
    if days > 90:
        return "DISABLE"
    elif days > 30:
        return "REVIEW"
    else:
        return "ACTIVE"


def save_checkin_data(data, department, status):
    """
    Writes the employee information
    to checkin_data.txt.
    """
    with open("checkin_data.txt", "w") as file:

        file.write("Employee Check-In Report\n")
        file.write("-------------------------\n")
        file.write(f"Name: {data['name']}\n")
        file.write(f"Department: {department}\n")
        file.write(f"Last Check-in: {data['checkin_date']}\n")
        file.write(
            f"Days Since Check-in: {data['days_since_checkin']}\n"
        )
        file.write(f"Status: {status}\n")


def run():

    # Get information from user_input.py
    data = user_input.get_user_data()

    # Verify employee name
    if not verify_name(data["name"]):
        print(f"\nERROR: '{data['name']}' is not an approved employee.")
        return

    # Ask for department
    department = input("What department are you in? ").strip()

    # Verify department
    if not verify_department(department):
        print(f"\nERROR: '{department}' is not a valid department.")
        return

    # Determine employee status
    status = determine_status(data["days_since_checkin"])

    # Save results
    save_checkin_data(data, department, status)

    print("\nVerification successful!")
    print(f"Employee: {data['name']}")
    print(f"Department: {department}")
    print(f"Status: {status}")
    print("Results have been saved to checkin_data.txt")


if __name__ == "__main__":
    run()