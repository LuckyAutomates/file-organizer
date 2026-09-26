# file-organizer
A Python automation script that organizes files by extension.
# File Organizer (Python Automation)

## 📌 Overview
This project is a simple yet powerful **file organizer** written in Python.  
It automatically sorts files in a chosen folder into subfolders based on their extensions.  
For example:
- `.exe` → Installers
- `.7z`, `.rar`, `.tar.gz` → Archives
- `.dll` → DLLs
- `.lnk` → Shortcuts  
…and any other extension gets its own folder automatically.

## 🚀 Features
- Auto‑detects file extensions and creates folders dynamically.
- Moves files into categorized subfolders.
- Generates a **log file (`organized_log.txt`)** with timestamps for every action.
- Includes error handling to prevent crashes if a file can’t be moved.
- Easy to customize for different file types.

## 🛠️ Technologies Used
- Python 3.x
- Standard libraries: `os`, `shutil`, `datetime`

## 📂 How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/LuckyAutomates/file-organizer.git
