import os
import json
import shutil
import argparse

def find_and_replace_duplicated(old_folder, new_folder):
    # Get list of filenames in both old and new folders
    old_files = os.listdir(old_folder)
    new_files = os.listdir(new_folder)

    # Find the set of duplicated filenames in both old and new folders
    duplicated_files = set(old_files) & set(new_files)

    # Loop through each duplicated filename
    for filename in duplicated_files:
        # Create the file paths for the old and new files
        old_file_path = os.path.join(old_folder, filename)
        new_file_path = os.path.join(new_folder, filename)
        # Overwrite the new file with the old file
        shutil.copy2(old_file_path, new_file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Paths")
    parser.add_argument('--old_file_path', help='Path to the old file')
    parser.add_argument('--new_file_path', help='Path to the new file')
    args = parser.parse_args()
    old_folder = args.old_file_path
    new_folder = args.new_file_path
    find_and_replace_duplicated(old_folder, new_folder)