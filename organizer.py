import os
import shutil
import sys

if "--help" in sys.argv:
    print("""
Smart File Organizer

Usage:
    python3 organizer.py [folder]
    python3 organizer.py [folder] --dry-run

Examples:
    python3 organizer.py Downloads
    python3 organizer.py Downloads --dry-run
""")
    sys.exit(0)

folder = "."
dry_run = False

for arg in sys.argv[1:]:
    if arg == "--dry-run":
        dry_run = True
    else:
        folder = arg

if not os.path.isdir(folder):
    print(f"Error: '{folder}' is not a valid folder.")
    sys.exit(1)

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}

for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)

    if not os.path.isfile(file_path):
        continue

    extension = os.path.splitext(filename)[1].lower()

    destination = None

    for category, extensions in categories.items():
        if extension in extensions:
            destination = category
            break

    if destination is None:
       destination = "Others"

    destination_folder = os.path.join(folder, destination)
    destination_path = os.path.join(destination_folder, filename)

    if os.path.exists(destination_path):
        name, extension = os.path.splitext(filename)
        counter = 1

        while os.path.exists(destination_path):
            new_filename = f"{name}_{counter}{extension}"
            destination_path = os.path.join(destination_folder, new_filename)
            counter += 1

    if dry_run:
        print(f"[DRY RUN] Would move: {filename} -> {destination}/")
    else:
        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(file_path, destination_path)
        print(f"Moved: {filename} -> {destination}/")

print("\nFile organization complete!")
