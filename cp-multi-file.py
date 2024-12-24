import os 
import shutil

def copy_file_multiple_times(source_files, destination_folder, num_copies):
    # Ensure the destination folder exists, if not, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate through each source file
    for source_file in source_files:
        # Check if the source file exists
        if not os.path.exists(source_file):
            print(f"Source file does not exist: {source_file}")
            continue

        # Get the file name from the source file path
        file_name = os.path.basename(source_file)
        
        # Copy the file multiple times
        for i in range(1, num_copies + 1):
            destination_file = os.path.join(destination_folder, f"{i}_{file_name}")
            try:
                shutil.copy(source_file, destination_file)
                print(f"Copied: {source_file} -> {destination_file}")
            except Exception as e:
                print(f"Error copying file {source_file} to {destination_file}: {e}")

# Example Usage
source_files = [
    r'C:\path\to\your\file1.txt',
    r'C:\path\to\your\file2.txt'
]  # List of source files to copy

destination_folder = r'C:\path\to\destination\folder'  # Ensure paths are correct
num_copies = 2500  # Number of copies you want to make for each file

copy_file_multiple_times(source_files, destination_folder, num_copies)
