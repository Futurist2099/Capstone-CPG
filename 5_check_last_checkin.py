"""
check_last_checkin.py (simple version)

Asks for an employee's name and how many days since their last check-in,
then saves that info to a file for checkin_status.py to use.
"""

# Load the approved names from employees_list.csv into a variable
valid_names_raw = open("employees_list.csv", "r").read()

VALID_NAMES = []
lines = valid_names_raw.strip().split("\n")
for line in lines[1:]:  # skip the header row
    name = line.split(",")[0]
    VALID_NAMES.append(name)

# STATIC VARIABLE: stays the same total across every employee we enter
employees_verified = 0

# This list will hold everyone we enter this run
records = []

print("Enter employee check-ins. Type 'done' when finished.\n")

while True:
    # DYNAMIC VARIABLE: a new value every time through the loop
    name = input("Employee name (or 'done' to finish): ")

    # CONDITIONAL LOGIC: this is how the loop knows when to stop
    if name == "done":
        break

    # CONDITIONAL LOGIC: reject names not on the approved list
    if name.strip().lower() not in [valid.lower() for valid in VALID_NAMES]:
        print(f"'{name}' is not on the approved list. Please try again.\n")
        continue

    days = input(f"How many days since {name}'s last check-in? ")

    # CONDITIONAL LOGIC: make sure they typed a number
    if not days.isdigit():
        print("Please enter a number.\n")
        continue

    days = int(days)
    records.append((name, days))
    employees_verified = employees_verified + 1
    print(f"Saved {name}: {days} days.\n")

# FILE CREATION: write everything we collected to a file
with open("checkin_data.txt", "w") as f:
    for name, days in records:
        f.write(f"{name},{days}\n")

print(f"\nDone! {employees_verified} employee(s) saved to checkin_data.txt")