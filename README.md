# Smart File Organizer

A Python-based command-line utility that automatically organizes files into categorized folders based on their file extensions.

The project is lightweight, practical, and runs locally without external Python packages.

---

# Features

- Automatically categorizes files by extension
- Supports Images, Documents, Videos, Audio, and Archives
- Moves unsupported file types into `Others/`
- Supports custom folder paths
- Provides a `--dry-run` mode
- Prevents duplicate files from being overwritten
- Automatically creates destination folders
- Includes a command-line help menu
- Requires no external Python packages
- Works completely locally
- Uses Git and GitHub for version control

---

# Supported File Categories

| File Type | Folder |
|---|---|
| JPG, JPEG, PNG, GIF, WEBP | Images |
| PDF, DOC, DOCX, TXT, PPT, PPTX, XLS, XLSX | Documents |
| MP4, MKV, AVI, MOV | Videos |
| MP3, WAV, FLAC | Audio |
| ZIP, RAR, 7Z, TAR, GZ | Archives |
| Other extensions | Others |

---

# How It Works

The program:

1. Takes a folder path from the command line.
2. Scans the files inside the folder.
3. Detects each file's extension.
4. Matches the extension with a category.
5. Creates the required folder.
6. Moves the file.
7. Checks for duplicate filenames.
8. Creates a new filename when a duplicate exists.

---

# Example

## Before

```text
Downloads/
├── photo.jpg
├── resume.pdf
├── movie.mp4
├── song.mp3
├── backup.zip
└── data.csv

## After
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── resume.pdf
├── Videos/
│   └── movie.mp4
├── Audio/
│   └── song.mp3
├── Archives/
│   └── backup.zip
└── Others/
    └── data.csv


# Requirements
Python 3
Linux / WSL / macOS / Windows
No external Python packages required
# Installation
## Clone the Repository
git clone https://github.com/hxrshits/smart-file-organizer.git
## Enter the Project Directory
cd smart-file-organizer
## Check Python
python3 --version
# Usage
## Organize a Folder
python3 organizer.py Downloads

Replace Downloads with the folder you want to organize.

## Dry Run

Preview changes without moving files:

python3 organizer.py Downloads --dry-run

Example:

[DRY RUN] Would move: photo.jpg -> Images/
[DRY RUN] Would move: resume.pdf -> Documents/
[DRY RUN] Would move: movie.mp4 -> Videos/

File organization complete!
## Help
python3 organizer.py --help

### Output:

Smart File Organizer

Usage:
    python3 organizer.py [folder]
    python3 organizer.py [folder] --dry-run

Examples:
    python3 organizer.py Downloads
    python3 organizer.py Downloads --dry-run
# Current Directory

If no folder is provided:

python3 organizer.py
# Duplicate File Protection

The program prevents existing files from being overwritten.

For example:

Images/
├── photo.jpg
└── photo_1.jpg

If another duplicate is found:

Images/
├── photo.jpg
├── photo_1.jpg
└── photo_2.jpg
# Safety

The --dry-run option allows users to preview file movements before making changes.

python3 organizer.py Downloads --dry-run

Always use --dry-run first when working with an important folder.

# Project Structure
smart-file-organizer/
│
├── organizer.py
├── README.md
└── .gitignore
# Technologies Used
Python 3
Linux / WSL
Git
GitHub
# Python Modules
os — filesystem operations
shutil — moving files
sys — command-line arguments
# Testing

The project was tested with multiple file types.

## Tested functionality:

Image categorization
Document categorization
Video categorization
Audio categorization
Archive categorization
Unknown file categorization
Duplicate filename handling
Custom folder paths
Dry-run mode
Help command

## Test command:

python3 organizer.py test_downloads --dry-run
# Future Improvements
Recursive folder scanning
More file extensions
Custom category configuration
Interactive CLI
Undo functionality
File movement logs
File size/date-based organization
Configuration file support
Windows GUI
Scheduled automatic organization
Background folder monitoring
# Why This Project?

This project was built to gain practical experience with:

Python scripting
File-system automation
Command-line interfaces
Linux / WSL
Git and GitHub
Automation
Software documentation

The goal was to create a small utility that is actually useful rather than just a demonstration program.

# Author

Harshit Saini

B.Tech — Electronics & Communication Engineering (AIML)

GitHub: https://github.com/hxrshits

# License

This project is intended for educational and personal use.
