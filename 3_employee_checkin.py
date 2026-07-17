def get_department():

    department = input(
        "What department are you in? "
    )

    return department

import csv


VALID_DEPARTMENTS = []


with open("employees_list.csv", newline="") as csvfile:

    reader = csv.DictReader(csvfile)

    for row in reader:

        VALID_DEPARTMENTS.append(
            row["Department"]
        )



def verify_department(department):

    """
    Checks dynamic department input
    against static CSV departments.
    """

    return department.strip().lower() in [
        dept.lower()
        for dept in VALID_DEPARTMENTS
    ]