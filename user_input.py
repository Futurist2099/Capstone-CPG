

from datetime import datetime, date


def ask_name():
    """Ask the user for their name and return it as a string."""
    name = input("What is your name? ").strip()
    return name


def ask_last_checkin():
    """
    Ask the user for their last check-in date.
    Keeps asking until a valid date in YYYY-MM-DD format is entered.
    Returns a datetime.date object.
    """
    while True:
        date_str = input("When is your last check-in at work? (YYYY-MM-DD): ").strip()
        try:
            checkin_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            return checkin_date
        except ValueError:
            print("That doesn't look like a valid date. Please use YYYY-MM-DD format.\n")


def days_since_checkin(checkin_date):
    """Calculate the number of days between today and the check-in date."""
    today = date.today()
    delta = today - checkin_date
    return delta.days


def get_user_data():
    """
    Runs the full input + verification flow for File 1.
    Returns a dictionary with name, checkin_date, and days_since_checkin.
    """
    name = ask_name()
    checkin_date = ask_last_checkin()
    days = days_since_checkin(checkin_date)

    return {
        "name": name,
        "checkin_date": checkin_date,
        "days_since_checkin": days
    }


# This block only runs when file1.py is executed directly (not when imported).
# It lets you test File 1 completely on its own before adding File 2.
if __name__ == "__main__":
    data = get_user_data()
    print("\n--- Collected Data ---")
    print(f"Name: {data['name']}")
    print(f"Last check-in: {data['checkin_date']}")
    print(f"Days since check-in: {data['days_since_checkin']}")
