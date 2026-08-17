import json
from pathlib import Path


CASES_DIR = Path("cases")


def save_case(case):
    CASES_DIR.mkdir(exist_ok=True)

    safe_name = case["name"].strip().lower().replace(" ", "_")
    file_path = CASES_DIR / f"{safe_name}.json"

    with open(file_path, "w") as file:
        json.dump(case, file, indent=4)

    return file_path

def list_cases():
    CASES_DIR.mkdir(exist_ok=True)

    case_files = list(CASES_DIR.glob("*.json"))
    cases = []

    for file_path in case_files:
        with open(file_path, "r") as file:
            case = json.load(file)

        cases.append({
            "data": case,
            "file_path": file_path,
        })

    return cases