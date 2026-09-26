import os
import shutil
from datetime import datetime

# Define categories for common extensions
EXTENSION_MAP = {
    "Installers": [".exe", ".msi"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".tar.gz"],
    "DLLs": [".dll"],
    "Shortcuts": [".lnk"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
}

LOG_FILE = "organized_log.txt"


def log_action(message: str) -> None:
    """Write a timestamped log entry."""
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")


def get_category(extension: str) -> str:
    """Return folder name based on extension, or use extension itself."""
    for category, extensions in EXTENSION_MAP.items():
        if extension.lower() in extensions:
            return category
    return extension[1:].upper() + "_files"  # e.g. ".py" → "PY_files"


def organize_files(folder: str) -> None:
    """Organize files in the given folder into subfolders by extension."""
    if not os.path.isdir(folder):
        print("Invalid folder path.")
        return

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            if not ext:
                continue  # skip files without extension

            category = get_category(ext)
            target_folder = os.path.join(folder, category)

            os.makedirs(target_folder, exist_ok=True)

            try:
                shutil.move(file_path, os.path.join(target_folder, filename))
                log_action(f"Moved '{filename}' → {category}")
            except Exception as e:
                log_action(f"Error moving '{filename}': {e}")


if __name__ == "__main__":
    folder_path = input("Enter the folder path to organize: ").strip()
    organize_files(folder_path)
    print("✅ Files organized successfully! Check organized_log.txt for details.")
