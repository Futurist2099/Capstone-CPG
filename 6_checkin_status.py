"""
checkin_status.py (simple version)

Reads the employee check-in data saved by check_last_checkin.py,
then decides each employee's status based on how many days it's been.
"""

# STATIC VARIABLE: keeps a running total across every employee, doesn't reset
disable_count = 0
review_count = 0
active_count = 0

# This list will hold the results for everyone we process
results = []

# Read each line from the file File 1 created
with open("checkin_data.txt", "r") as f:
    for line in f:
        line = line.strip()

        # CONDITIONAL LOGIC: skip any blank lines in the file
        if line == "":
            continue

        # Each line looks like "John,95" -- split it into two pieces
        name, days = line.split(",")
        days = int(days)

        # CONDITIONAL LOGIC: this is the status rule from the spec
        if days > 90:
            status = "DISABLE"
            disable_count = disable_count + 1
        elif days > 30:
            status = "REVIEW"
            review_count = review_count + 1
        else:
            status = "ACTIVE"
            active_count = active_count + 1

        results.append((name, days, status))
        print(f"{name}: {days} days -> {status}")

# FILE CREATION: write everything out to a report file
with open("status_report.txt", "w") as f:
    for name, days, status in results:
        f.write(f"{name}: {days} days -> {status}\n")

    f.write(f"\nDISABLE: {disable_count}\n")
    f.write(f"REVIEW: {review_count}\n")
    f.write(f"ACTIVE: {active_count}\n")

print("\nDone! Results saved to status_report.txt")