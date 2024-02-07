import os
import shutil
import re
from datetime import datetime

def clean_directory_name(path):
    log_path =  f'{timestamp}_org_log.txt'
    with open(log_path, 'a', encoding='utf-8') as log:
        if not os.path.exists(path):
            log.write(f"The source folder '{path}' does not exist.")
            return

        folders = os.listdir(path)
        for folder in folders:
            # Use a regular expression to remove "[something]" from the folder name
            cleaned_folder_name = re.sub(r'\[.*?\]', '', folder).strip()
            # Create a new folder path with the cleaned name
            new_folder_path = os.path.join(path, cleaned_folder_name)
            # Rename the folder
            os.rename(os.path.join(path, folder), new_folder_path)
            # Print a message indicating the renaming
            log.write(f"Renamed '{folder}' to '{cleaned_folder_name}'.\n")

        # Print a message indicating that the folder names have been cleaned
        print("Cleaning folder names completed.")
        log.write(f"Cleaning folder names completed.\n")
    shutil.move(log_path, os.path.join(path, log_path))


def organiser(path):
    log_path = f'{timestamp}_org_log.txt'
    with open(log_path, 'a', encoding='utf-8') as log:
        if not os.path.exists(path):
            log.write(f"The source folder '{path}' does not exist.")
            return
        files = os.listdir(path)
        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:]
            if os.path.exists(os.path.join(path, extension)):
                shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
            else:
                os.mkdir(os.path.join(path, extension))
                shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
            log.write(f"Moved '{file}' to '{path}\\{extension}'.\n")

        # Print a message indicating that file organization has been completed
        print("Organizing files completed.")
        log.write(f"Organizing files completed.\n")
    shutil.move(log_path, os.path.join(path, log_path))


def anime_organiser(path):
    # log file for this function
    log_path = f'{timestamp}_org_log.txt'
    with open(log_path, 'a', encoding='utf-8') as log:
        if not os.path.exists(path):
            log.write(f"The source folder '{path}' does not exist.\n")
            return
        files = os.listdir(path)
        for file in files:
            if file.lower().endswith(".mkv"):
                match = re.match(r'^(.+?)\s*-\s*\d+', file)
                if match:
                    common_name = match.group(1).strip()
                else:
                    common_name = os.path.splitext(file)[0]

                # Create a folder with the common name if it doesn't exist
                target_folder = os.path.join(path, common_name)
                os.makedirs(target_folder, exist_ok=True)
                # Move the file to the target folder
                shutil.move(os.path.join(path, file), os.path.join(target_folder, file))
                movemsg = f"Moved '{file}' to '{common_name}' folder.\n"
                log.write(movemsg)

        # Print a message indicating that file organization has been completed
        endmsg = "Organizing files completed."
        print(endmsg)
        log.write(endmsg + "\n")
    shutil.move(log_path, os.path.join(path,log_path))

timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
finish = 1

while finish == 1:
    pick = input("1. Folder Organiser by Extension\n2. Series Organiser\n3. Folder Name Cleaner\n")
    if pick == "1":
        path = input("Enter Folder Path: ")
        organiser(path)
        finish = 0
    elif pick == "2":
        path = input("Enter Folder Path: ")
        anime_organiser(path)
        finish = 0
    elif pick == "3":
        path = input("Enter Folder Path: ")
        clean_directory_name(path)
        finish = 0
    else:
        print("Wrong Input. Please try again\n")
