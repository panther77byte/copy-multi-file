# File Copy Script  

A Python script to copy files multiple times efficiently, ideal for testing, data duplication, or automation tasks.  

---

## Features  
- **Bulk File Duplication**: Copy one or more source files thousands of times.  
- **Customizable**: Easily configure the source files, destination folder, and number of copies.  
- **Error Handling**: Skips non-existent files and provides clear error messages.  
- **Windows-Friendly**: Works seamlessly with Windows file paths.  

---

## Use Case  
This script is perfect for:  
1. **Testing**: Simulate file system loads by creating thousands of identical files.  
2. **Automation**: Quickly duplicate files for testing automation workflows.  
3. **Development**: Generate large datasets for experiments or debugging.  

---

## Requirements  

- **Python 3.x**  
- **Libraries**: `os`, `shutil` (both included in the Python standard library).  

---

## Setup  

1. Clone this repository:  
   ```bash
   git clone https://github.com/panther77byte/copy-multi-file.git
   cd copy-multi-file
2. Edit the script to match your file paths and preferences: 
   ```bash
   source_files = [
    r'C:\path\to\your\file1.txt',
    r'C:\path\to\your\file2.txt'
   ]  # List of source files to copy

   destination_folder = r'C:\path\to\destination\folder'  # Destination directory
   num_copies = 2500  # Number of copies to create for each file
3. Run the script: 
   ```bash
   python cp-multi-file.py

---

## Example

- **Source Files:
   ```bash
   C:\path\to\file1.txt  
   C:\path\to\file2.txt

- **Destination Folder: 
   ```bash
   C:\path\to\destination-folder

- **Number of Copies:
   ```bash
   2500

---

## Requirements  
- **The script will create copies in the destination folder like:
  ```bash
  1_file1.txt  
  2_file1.txt  
  ...  
  2500_file1.txt  

  1_file2.txt  
  2_file2.txt
  ...  
  2500_file2.txt

  ---

## Error Handling

- **If a source file doesn’t exist, the script will skip it and display a message:
   ```bash
   Source file does not exist: C:\path\to\missing-file.txt

- **Errors during copying are logged with details:
   ```bash
   Error copying file C:\path\to\file1.txt to C:\path\to\destination-folder\1_file1.txt: [Error Message]
