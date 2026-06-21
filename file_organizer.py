import os
import shutil

# Folder to organize
source_folder = r"C:\Users\Lenovo\Downloads"

# File categories and their associated extensions
file_types = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg"
    ],
    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"
    ],
    "Documents": [
        ".pdf", ".doc", ".docx", ".txt",
        ".ppt", ".pptx", ".xls", ".xlsx", ".csv"
    ],
    "Softwares": [
        ".exe", ".msi", ".apk", ".dmg", ".pkg", ".winmd"
    ],
    "Music": [
        ".mp3", ".wav", ".aac", ".flac", ".ogg"
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz"
    ]
}

# Loop through every item in the source folder
for file_name in os.listdir(source_folder):

    # Create the full path of the current item
    file_path = os.path.join(source_folder, file_name)

    # Skip folders and process only files
    if not os.path.isfile(file_path):
        continue

    # Get the file extension in lowercase
    extension = os.path.splitext(file_name)[1].lower()

    # Default category
    folder_name = "Others"

    # Find the matching category
    for category, extensions in file_types.items():
        if extension in extensions:
            folder_name = category
            break

    # Create the destination folder if it doesn't exist
    destination_folder = os.path.join(source_folder, folder_name)
    os.makedirs(destination_folder, exist_ok=True)

    # Move the file
    destination_path = os.path.join(destination_folder, file_name)
    shutil.move(file_path, destination_path)

    print(f"✅ {file_name} was moved to '{folder_name}'")

print("\n🎉 File organization completed successfully!")