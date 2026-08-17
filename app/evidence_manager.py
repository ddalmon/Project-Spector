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
        return

    if not evidence_path.is_dir():
        print("\nPath is not a directory.")
        return

    print("\n=== Evidence Found ===")

    found_files = 0

    for file in evidence_path.iterdir():
        if file.is_file():

            extension = file.suffix.lower()

            if extension in SUPPORTED_EXTENSIONS:
                evidence_type = SUPPORTED_EXTENSIONS[extension]

                print(
                    f"{evidence_type:<10} {file.name}"
                )

                found_files += 1

    if found_files == 0:
        print("No supported evidence files found.")