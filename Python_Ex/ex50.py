import shutil
import os

def backup_files():
    source_folder = "source_files"
    backup_folder = "backup_files"
    log_file = "backup.log"

    os.makedirs(backup_folder, exist_ok=True)

    copied_files = set()

    with open(log_file, "a") as log:
        for file_name in os.listdir(source_folder):

            source_path = os.path.join(source_folder, file_name)
            backup_path = os.path.join(backup_folder, file_name)

            if file_name in copied_files:
                continue

            try:
                shutil.copy(source_path, backup_path)
                copied_files.add(file_name)
                log.write(f"Copied: {file_name}\n")

            except FileNotFoundError:
                log.write(f"Missing file: {file_name}\n")

    return "Backup completed successfully"


print(backup_files())