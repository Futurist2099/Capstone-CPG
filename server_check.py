print ("Hello world - server check initiated...")

employees = []

with open("data/employee.txt", "r") as file:
    for line in file:
        line = line.strip()

        if line == "":
            continue

        parts = line.split(",")

        if len(parts) != 3:
            print(f"Skipping bad line: {line}")
            continue

        username = parts[0]
        department = parts[1]
        days = parts[2]

        if not days.isdigit():
            print(f"Skipping invalid login value: {line}")
            continue

        days = int(days)

        employee_record = (username, department, days)

        employees.append(employee_record)

print("ACCOUNT AUDIT REPORT")
print("====================")

for employee in employees:
    username = employee[0]
    department = employee[1]
    days = employee[2]

    if days > 90:
        status = "DISABLE"
    elif days > 30:
        status = "REVIEW"
    else:
        status = "ACTIVE"

    print(f"{username} | {department} | {days} days | {status}")