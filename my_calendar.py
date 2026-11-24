import calendar
from datetime import datetime

while True:
    print("\n" + "=" * 35)
    print("       PYTHON CALENDAR")
    print("=" * 35)

    print("1. View Current Month")
    print("2. View Specific Month")
    print("3. View Full Year")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        now = datetime.now()
        print("\n", calendar.month(now.year, now.month))

    elif choice == "2":
        year = int(input("Enter year: "))
        month = int(input("Enter month (1-12): "))

        if 1 <= month <= 12:
            print("\n", calendar.month(year, month))
        else:
            print("Invalid month!")

    elif choice == "3":
        year = int(input("Enter year: "))
        print("\n", calendar.calendar(year))

    elif choice == "4":
        print("\nCalendar closed. Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")