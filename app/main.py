from case_manager import create_case
from storage import save_case


def main():
    print("==============================")
    print("       PROJECT SPECTOR")
    print("==============================")

    case = create_case()
    file_path = save_case(case)

    print(f"\nInvestigation '{case['name']}' is ready.")
    print(f"Case saved to: {file_path}")


if __name__ == "__main__":
    main()