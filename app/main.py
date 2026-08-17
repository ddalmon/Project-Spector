from case_manager import create_case
from storage import save_case, list_cases


def show_menu():
    print("\n==============================")
    print("       PROJECT SPECTOR")
    print("==============================")
    print("1. Create Case")
    print("2. View Cases")
    print("3. Exit")


def view_cases():
    cases = list_cases()

    if not cases:
        print("\nNo saved cases found.")
        return

    print("\n=== Saved Cases ===")

    for index, case_info in enumerate(cases, start=1):
        case = case_info["data"]

        print(
            f"{index}. {case['name']} | "
            f"{case['location']} | "
            f"{case['date']}"
        )

    selection = input(
        "\nSelect a case number or press Enter to return: "
    ).strip()

    if not selection:
        return

    try:
        case_index = int(selection) - 1

        if 0 <= case_index < len(cases):
            selected_case = cases[case_index]["data"]

            print("\n=== Investigation Case ===")
            print(f"Name:     {selected_case['name']}")
            print(f"Location: {selected_case['location']}")
            print(f"Date:     {selected_case['date']}")
        else:
            print("\nInvalid case selection.")

    except ValueError:
        print("\nPlease enter a valid number.")


def main():
    while True:
        show_menu()

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            case = create_case()
            file_path = save_case(case)

            print(f"\nInvestigation '{case['name']}' is ready.")
            print(f"Case saved to: {file_path}")

        elif choice == "2":
            view_cases()

        elif choice == "3":
            print("\nExiting Project Spector.")
            break

        else:
            print("\nInvalid selection. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()