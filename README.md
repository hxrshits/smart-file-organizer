# Smart File Organizer

A simple Python utility that automatically organizes files into folders based on their file type.

## Features

- Organizes images, documents, videos, audio and archives
- Moves unknown file types into `Others/`
- Supports custom folder paths
- `--dry-run` mode to preview changes without moving files
- Duplicate filename protection
- Simple command-line interface
- Zero external dependencies

## Categories

| File Type | Folder |
|---|---|
| JPG, PNG, GIF, WEBP | Images |
| PDF, DOCX, TXT, PPTX, XLSX | Documents |
| MP4, MKV, AVI, MOV | Videos |
| MP3, WAV, FLAC | Audio |
| ZIP, RAR, 7Z, TAR, GZ | Archives |
| Other extensions | Others |

## Requirements

- Python 3
- Linux / WSL / macOS / Windows

## Usage

Organize a folder:

```bash
python3 organizer.py Downloads
