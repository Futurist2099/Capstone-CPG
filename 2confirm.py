import csv
import user_input  # this file must have a get_user_data() function in it

# STEP 1: Build the list of approved employee names from employees_list.csv
VALID_NAMES = []

with open("employees_list.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        VALID_NAMES.append(row["Name"])


def verify_name(name):
    """Return True if the name is in the approved list (case-insensitive)."""
    return name.strip().lower() in [valid.lower() for valid in VALID_NAMES]


def get_verified_user_data():
    """
    Keeps asking for check-in info until the entered name matches
    someone on the approved list. Returns the final, verified data.
    """
    while True:
        data = user_input.get_user_data()

        if verify_name(data["name"]):
            return data
        else:
            print(f"\n'{data['name']}' is not on the approved list. Please try again.\n")


def determine_status(days):
    """
    Business rule: decide status based on days since last check-in.
    """
    if days > 90:
        return "DISABLE"
    elif days > 30:
        return "REVIEW"
    else:
        return "ACTIVE"


def run():
    """Main flow: verify the user, compute their status, and save the result."""

    # Ask questions and verify the name against the approved list
    data = get_verified_user_data()

    # Figure out ACTIVE / REVIEW / DISABLE based on days since check-in
    status = determine_status(data["days_since_checkin"])

    # Show the result on screen
    print("\n--- Final Result ---")
    print(f"Name: {data['name']}")
    print(f"Last check-in: {data['checkin_date']}")
    print(f"Days since check-in: {data['days_since_checkin']}")
    print(f"Status: {status}")

    # Save the result to checkin_data.txt so other scripts can use it
    # "a" = append mode, so we add to the file instead of erasing it
    with open("checkin_data.txt", "a") as f:
        f.write(f"{data['name']},{data['days_since_checkin']}\n")

    print(f"\nSaved to checkin_data.txt: {data['name']},{data['days_since_checkin']}")

    return status


# This only runs if the file is executed directly (not imported by another script)
if __name__ == "__main__":
    run()



        
        
#twerk