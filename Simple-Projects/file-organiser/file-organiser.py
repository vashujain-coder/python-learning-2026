import os
import shutil
from datetime import datetime

FOLDERS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.csv', '.pptx'],
    'Code': ['.py', '.js', '.html', '.css', '.json', '.java', '.cpp'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac'],
    'Other': []
}

def get_folder(extension):
    extension = extension.lower()
    for folder, extensions in FOLDERS.items():
        if extension in extensions:
            return folder
    return 'Other'

def organise_folder(path):
    if not os.path.exists(path):
        print(f"❌ Error: Path '{path}' does not exist.")
        return

    summary = {}
    moved_count = 0

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        if not ext:
            folder_name = 'Other'
        else:
            folder_name = get_folder(ext)

        target_dir = os.path.join(path, folder_name)

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        try:
            shutil.move(file_path, os.path.join(target_dir, filename))
            summary[filename] = folder_name
            moved_count += 1
            print(f"Moved: {filename} → {folder_name}/")
        except Exception as e:
            print(f"Failed to move {filename}: {e}")

    print(f"\n✅ Organised {moved_count} files successfully!")
    generate_report(summary, path)

def generate_report(moved_files, path):
    if not moved_files:
        return

    report_path = os.path.join(path, "organised_report.txt")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"Folder Organised Report\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total files moved: {len(moved_files)}\n")
        f.write("-" * 60 + "\n\n")

        for file, folder in moved_files.items():
            f.write(f"{file}  →  {folder}\n")

    print(f"📄 Report saved as: organised_report.txt")

if __name__ == "__main__":
    print("=== File Organizer Tool ===\n")
    while True:
        path = input("Enter the full path of the folder you want to organise: ").strip()
        if os.path.exists(path):
            break
        print("❌ Path does not exist. Please try again.\n")

    organise_folder(path)