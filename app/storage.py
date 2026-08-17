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