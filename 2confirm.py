

import file1


# The "list" that names must match against.
# Replace these with your real names, or load them from a file/database
# (e.g., a CSV of employees) if you have a real source of truth.
VALID_NAMES = ["Alice", "Bob", "Charlie", "Dana"]


def verify_name(name):
    """Return True if the name is in the approved list (case-insensitive)."""
    return name.strip().lower() in [valid.lower() for valid in VALID_NAMES]


def get_verified_user_data():
    """
    Repeats File 1's question flow until the entered name matches
    the approved list. Returns the final, verified data dictionary.
    """
    while True:
        data = file1.get_user_data()
        if verify_name(data["name"]):
            return data
        else:
            print(f"\n'{data['name']}' is not on the approved list. Please try again.\n")


def determine_status(days):
    """
    Apply the business rule to decide status based on days
    since the employee's last check-in.
    """
    if days > 90:
        return "DISABLE"
    elif days > 30:
        return "REVIEW"
    else:
        return "ACTIVE"


def run():
    """Main flow: verify the user, then compute and display their status."""
    data = get_verified_user_data()
    status = determine_status(data["days_since_checkin"])

    print("\n--- Final Result ---")
    print(f"Name: {data['name']}")
    print(f"Last check-in: {data['checkin_date']}")
    print(f"Days since check-in: {data['days_since_checkin']}")
    print(f"Status: {status}")

    return status


if __name__ == "__main__":
    run()
