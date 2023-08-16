import os
import json
import shutil

def find_duplicated_json_files(root_folders):
    # Dictionary to store filenames and their corresponding file paths
    file_dict = {}

    # Traverse through the directory trees of all root folders
    for root_folder in root_folders:
        for folder_name, subfolders, filenames in os.walk(root_folder):
            for filename in filenames:
                if filename.endswith('.json'):
                    file_path = os.path.join(folder_name, filename)
                    if filename in file_dict:
                        file_dict[filename].append(file_path)
                    else:
                        file_dict[filename] = [file_path]

    # Find duplicated JSON files
    duplicated_json_files = {filename: paths for filename, paths in file_dict.items() if len(paths) > 1}
    
    return duplicated_json_files

def overwrite_duplicated_files(source_folder, duplicated_files):
    for filename, paths in duplicated_files.items():
        source_path = paths[0]  # Select the first file path as the source
        for dest_path in paths[1:]:
            # Overwrite the content from the source file to the destination file
            with open(source_path, 'r') as source_file:
                data = json.load(source_file)
                with open(dest_path, 'w') as dest_file:
                    json.dump(data, dest_file, indent=4)

if __name__ == "__main__":
    root_folders = ["/Users/antonioyang/Documents/Python/copy_duplicated_file/old_file_annotated", "/Users/antonioyang/Documents/Python/copy_duplicated_file/new_file_non-annotated"]
    
    # Find duplicated JSON files in the specified root folders
    duplicated_json_files = find_duplicated_json_files(root_folders)
    
    # Overwrite duplicated JSON files in folder2 with files from folder1
    overwrite_duplicated_files(root_folders[0], duplicated_json_files)
