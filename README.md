Smart File Organizer

A Python-based command-line utility that automatically organizes files into categorized folders based on their file extensions.

The project is designed as a lightweight and practical file-management tool that can run locally on Linux, WSL, macOS, or Windows without external Python dependencies.

Features
Automatically categorizes files by extension
Supports Images, Documents, Videos, Audio, and Archives
Moves unsupported file types into Others/
Supports custom folder paths
Provides a --dry-run mode for safe previews
Prevents duplicate files from being overwritten
Automatically creates destination folders
Includes a command-line help menu
Requires no external Python packages
Works completely locally
Version controlled using Git and GitHub
Supported File Categories
File Type	Folder
JPG, JPEG, PNG, GIF, WEBP	Images
PDF, DOC, DOCX, TXT, PPT, PPTX, XLS, XLSX	Documents
MP4, MKV, AVI, MOV	Videos
MP3, WAV, FLAC	Audio
ZIP, RAR, 7Z, TAR, GZ	Archives
Other extensions	Others
How It Works

The program:

Takes a folder path from the command line.
Scans the files inside the folder.
Detects each file's extension.
Matches the extension with a predefined category.
Creates the required category folder.
Moves the file into the appropriate folder.
Checks for duplicate filenames.
Creates a new filename when a duplicate exists.
Example
Before
Downloads/
├── photo.jpg
├── resume.pdf
├── movie.mp4
├── song.mp3
├── backup.zip
└── data.csv
After
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
Requirements
Python 3
Linux / WSL / macOS / Windows
No external Python packages required
Installation
Clone the Repository
git clone https://github.com/hxrshits/smart-file-organizer.git
Enter the Project Directory
cd smart-file-organizer
Check Python
python3 --version
Usage
Organize a Folder
python3 organizer.py Downloads

Replace Downloads with the path of your target folder.

Dry Run

Before actually moving files, use --dry-run to preview the changes:

python3 organizer.py Downloads --dry-run

Example output:

[DRY RUN] Would move: photo.jpg -> Images/
[DRY RUN] Would move: resume.pdf -> Documents/
[DRY RUN] Would move: movie.mp4 -> Videos/

File organization complete!

Nothing is moved when using --dry-run.

Help

Display the available commands:

python3 organizer.py --help

Output:

Smart File Organizer

Usage:
    python3 organizer.py [folder]
    python3 organizer.py [folder] --dry-run

Examples:
    python3 organizer.py Downloads
    python3 organizer.py Downloads --dry-run
Current Directory

If no folder is provided, the program uses the current directory:

python3 organizer.py
Duplicate File Protection

The program prevents existing files from being overwritten.

For example, if photo.jpg already exists:

Images/
└── photo.jpg

and another file with the same name is moved, the program automatically creates:

Images/
├── photo.jpg
└── photo_1.jpg

If another duplicate exists:

Images/
├── photo.jpg
├── photo_1.jpg
└── photo_2.jpg
Safety

The project includes a --dry-run mode so users can preview file movements before making changes.

Example:

python3 organizer.py Downloads --dry-run

The program only modifies the folder that you explicitly provide.

Always use --dry-run first when working with an important folder.

Project Structure
smart-file-organizer/
│
├── organizer.py
├── README.md
└── .gitignore
Technologies Used
Python 3
Linux / WSL
Git
GitHub
Python Modules
os — filesystem operations
shutil — moving files
sys — command-line arguments
Example Output
Normal Mode
Moved: photo.jpg -> Images/
Moved: resume.pdf -> Documents/
Moved: movie.mp4 -> Videos/
Moved: song.mp3 -> Audio/
Moved: backup.zip -> Archives/
Moved: data.csv -> Others/

File organization complete!
Dry Run Mode
[DRY RUN] Would move: photo.jpg -> Images/
[DRY RUN] Would move: resume.pdf -> Documents/
[DRY RUN] Would move: movie.mp4 -> Videos/

File organization complete!
Testing

The project was tested using a local test directory containing multiple file types.

Tested Functionality
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
Test Command
python3 organizer.py test_downloads --dry-run
Future Improvements

Possible future improvements include:

Recursive folder scanning
Support for additional file extensions
Custom category configuration
Interactive CLI
Undo functionality
File movement logs
File size/date-based organization
Configuration file support
Windows GUI
Scheduled automatic organization
Background folder monitoring
Why This Project?

This project was built to gain practical experience with:

Python scripting
File-system automation
Command-line interfaces
Linux / WSL
Git and GitHub
Automation and problem solving
Software documentation

The goal was to create a small utility that is actually useful rather than just a demonstration program.

Author

Harshit Saini

B.Tech — Electronics & Communication Engineering (AIML)

GitHub: https://github.com/hxrshits

License

This project is intended for educational and personal use.
