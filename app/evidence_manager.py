from pathlib import Path


SUPPORTED_EXTENSIONS = {
    ".mp4": "VIDEO",
    ".mov": "VIDEO",
    ".avi": "VIDEO",
    ".wav": "AUDIO",
    ".mp3": "AUDIO",
    ".csv": "SENSOR",
    ".txt": "NOTES",
}


def import_evidence():
    folder_path = input(
        "\nEnter evidence folder path: "
    ).strip()

    evidence_path = Path(folder_path)

    if not evidence_path.exists():
        print("\nFolder not found.")
        return []

    if not evidence_path.is_dir():
        print("\nPath is not a directory.")
        return []

    evidence_records = []

    print("\n=== Evidence Found ===")

    for file in evidence_path.iterdir():
        if file.is_file():
            extension = file.suffix.lower()

            if extension in SUPPORTED_EXTENSIONS:
                evidence_type = SUPPORTED_EXTENSIONS[extension]

                evidence_record = {
                    "name": file.name,
                    "type": evidence_type,
                    "path": str(file),
                }

                evidence_records.append(evidence_record)

                print(
                    f"{evidence_type:<10} {file.name}"
                )

    if not evidence_records:
        print("No supported evidence files found.")

    return evidence_records