def create_case():
    print("\n=== Create New Investigation ===")

    case_name = input("Case name: ").strip()
    location = input("Location: ").strip()
    investigation_date = input("Investigation date: ").strip()

    print("\nCase Created")
    print("------------------------------")
    print(f"Name:     {case_name}")
    print(f"Location: {location}")
    print(f"Date:     {investigation_date}")
    print("------------------------------")

    return {
        "name": case_name,
        "location": location,
        "date": investigation_date,
    }

def case_menu(case):
    while True:
        print(f"\n=== {case['name']} ===")
        print("1. Import Evidence")
        print("2. View Evidence")
        print("3. Add Note")
        print("4. View Notes")
        print("5. Timeline")
        print("6. Return to Main Menu")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            print("\nImport Evidence coming in a future sprint.")

        elif choice == "2":
            print("\nView Evidence coming in a future sprint.")

        elif choice == "3":
            print("\nAdd Note coming in a future sprint.")

        elif choice == "4":
            print("\nView Notes coming in a future sprint.")

        elif choice == "5":
            print("\nTimeline coming in a future sprint.")

        elif choice == "6":
            break

        else:
            print("\nInvalid selection.")