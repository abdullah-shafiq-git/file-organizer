# Automated File Organizer Script 📂

A simple and efficient Python script to automatically clean up messy folders (like Downloads) by sorting files into categorized folders based on their extensions.

## Features
- Automatically detects file extensions (`.png`, `.pdf`, `.mp4`, `.zip`, etc.).
- Creates category folders (`Images`, `Documents`, `Videos`, `Archives`, `Programs`, etc.) dynamically.
- Moves uncategorized files into an `Others` folder safely.
- Built using Python's native modules (`os` and `shutil`), so no external libraries are required.

## Requirements
- Python 3.x installed on your system.

## How to Run
1. Open `organizer.py` and update the `TARGET_DIRECTORY` variable with the path of the folder you want to organize.
2. Run the script using your terminal:
   ```bash
   python organizer.py