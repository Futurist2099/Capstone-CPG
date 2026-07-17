import csv


def get_department():

    department = input(
        "What department are you in? "
    )

    return department



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



if __name__ == "__main__":

    department = get_department()

    if verify_department(department):
        print(
            f"{department} is a valid department."
        )
    else:
        print(
            f"{department} is not a valid department."
        )