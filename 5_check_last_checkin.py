"""
check_last_checkin.py (simple version)

Reads employee check-in data from checkin_data.txt, validates each
name against the approved list in employees_list.csv, and keeps
only the valid entries.
"""

# Load the approved names from employees_list.csv into a variable
valid_names_raw = open("employees_list.csv", "r").read()

VALID_NAMES = []
lines = valid_names_raw.strip().split("\n")
for line in lines[1:]:  # skip the header row
    name = line.split(",")[0]
    VALID_NAMES.append(name)

# STATIC VARIABLE: stays the same total across every record we process
employees_verified = 0

# This list will hold every valid record we find
records = []

# Read the existing check-in data instead of asking questions
with open("checkin_data.txt", "r") as f:
    for line in f:
        line = line.strip()

        # CONDITIONAL LOGIC: skip any blank lines in the file
        if line == "":
            continue

        # Each line looks like "Bob,22" -- split it into two pieces
        name, days = line.split(",")

        # CONDITIONAL LOGIC: reject names not on the approved list
        if name.strip().lower() not in [valid.lower() for valid in VALID_NAMES]:
            print(f"'{name}' is not on the approved list. Skipping.")
            continue

        # CONDITIONAL LOGIC: make sure days is a valid number
        if not days.isdigit():
            print(f"'{days}' is not a valid number of days for {name}. Skipping.")
            continue

        days = int(days)
        records.append((name, days))
        employees_verified = employees_verified + 1
        print(f"Verified {name}: {days} days.")

# FILE CREATION: write the verified records back out
with open("checkin_data.txt", "w") as f:
    for name, days in records:
        f.write(f"{name},{days}\n")

print(f"\nDone! {employees_verified} employee(s) verified and saved to checkin_data.txt")