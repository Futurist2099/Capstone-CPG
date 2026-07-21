def show_checkin_results():

    print("\n--- Check-In Data Results ---")

    with open("checkin_data.txt", "r") as f:
        for line in f:
            line = line.strip()

            if (
                line.startswith("Name:")
                or line.startswith("Department:")
                or line.startswith("Last Check-in:")
            ):
                print(line)


if __name__ == "__main__":
    show_checkin_results()