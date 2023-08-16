import os
import json
import shutil
import argparse

def find_and_replace_duplicated(old_folder, new_folder):
   # Walk through the directory tree rooted at old_folder
   for root, _, _ in os.walk(old_folder):
        # Get the list of filenames in the current old folder
        old_files = set(os.listdir(root))
        
        # Get the list of filenames in the new folder
        new_files = set(os.listdir(new_folder))
        
        # Find duplicated filenames in both old and new folders
        duplicated_files = old_files & new_files
        
        # Loop through each duplicated filename
        for filename in duplicated_files:
            # Create the file paths for the old and new files
            old_file_path = os.path.join(root, filename)
            new_file_path = os.path.join(new_folder, os.path.relpath(old_file_path, old_folder))
            
            # Check if the file already exists in the new folder
            if os.path.exists(new_file_path):
                # Overwrite the new file with the old file, preserving metadata
                shutil.copy2(old_file_path, new_file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Paths")
    parser.add_argument('--old_file_path', help='Path to the old file')
    parser.add_argument('--new_file_path', help='Path to the new file')
    args = parser.parse_args()
    old_folder = args.old_file_path
    new_folder = args.new_file_path
    find_and_replace_duplicated(old_folder, new_folder)