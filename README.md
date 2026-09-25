# Smart File Organizer

A simple Python CLI utility that automatically organizes files into folders based on their file type.

## Features

- Organizes images, documents, videos, audio, and archives
- Moves unknown file types into `Others/`
- Supports custom folder paths
- `--dry-run` mode to preview changes without moving files
- Duplicate filename protection
- Simple command-line interface
- Zero external dependencies

## Categories

| File Type | Folder |
|---|---|
| JPG, JPEG, PNG, GIF, WEBP | Images |
| PDF, DOC, DOCX, TXT, PPT, PPTX, XLS, XLSX | Documents |
| MP4, MKV, AVI, MOV | Videos |
| MP3, WAV, FLAC | Audio |
| ZIP, RAR, 7Z, TAR, GZ | Archives |
| Other extensions | Others |

## Requirements

- Python 3
- Linux / WSL / macOS / Windows
- No external Python packages required

## Usage

### Organize a folder

```bash
python3 organizer.py Downloads

# Preview changes with Dry Run

Use --dry-run to see what would be moved without actually moving any files.

python3 organizer.py Downloads --dry-run

# Show Help
python3 organizer.py --help
# Use the Current Directory

If no folder is specified, the current directory is used.

python3 organizer.py
#Example
##Before
Downloads/
├── photo.jpg
├── resume.pdf
├── movie.mp4
├── song.mp3
└── data.csv
##After
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── resume.pdf
├── Videos/
│   └── movie.mp4
├── Audio/
│   └── song.mp3
└── Others/
    └── data.csv
## Duplicate File Protection

If a file with the same name already exists in the destination folder, the program automatically creates a new filename.

Example:

photo.jpg
photo_1.jpg
photo_2.jpg

This prevents existing files from being overwritten.

# Safety

Use --dry-run before organizing an important folder.

The program only modifies the folder that you explicitly provide.

#Project Structure
smart-file-organizer/
├── organizer.py
├── README.md
└── .gitignore
#Technologies
Python
Linux / WSL
Git
GitHub
#Author

Harshit Saini

GitHub: hxrshits
