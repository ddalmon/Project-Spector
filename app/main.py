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


def main():
    print("==============================")
    print("       PROJECT SPECTOR")
    print("==============================")

    case = create_case()

    print(f"\nInvestigation '{case['name']}' is ready.")


if __name__ == "__main__":
    main()