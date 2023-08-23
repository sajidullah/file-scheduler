import shutil
import os
import datetime
import time

def backup_document(source_path, backup_folder):
    # Create a timestamp for the backup file
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"backup_{timestamp}.docx"

    # Create the full paths for source and backup files
    source_file = os.path.join(source_path)
    backup_file = os.path.join(backup_folder, backup_filename)

    try:
        # Copy the source file to the backup folder
        shutil.copy2(source_file, backup_file)
        print("Backup created successfully:", backup_file)
    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print("An error occurred:", e)

# Paths for source document and backup folder
source_path = r"C:\Users\sajid\Downloads\PhD_Thesis_2023_muni.docx"
backup_folder = r"G:\SQL"

# Set the desired time for backup (24-hour format, e.g., 02:00)
backup_time = "02:00"

while True:
    current_time = datetime.datetime.now().strftime("%H:%M")
    if current_time == backup_time:
        backup_document(source_path, backup_folder)
    time.sleep(60)  # Sleep for 60 seconds (1 minute)
