# ------------------ File Organizer Script ----------------- 

This Python script automates the organization of files within a specified directory by categorizing them into folders based on their file extensions. 
The script creates folders for different file types (e.g., Documents, Images, Videos, Music, Archives, CodeFiles) and moves the corresponding files into these folders.
This helps maintain a clean and organized directory structure, saving time and effort, and ensuring consistency.

## -------------- Objective ------------ 

The primary objective of this script is to automate the file organization process to:
  1. Maintain a clean and organized directory structure.
  2. Save time and effort by reducing manual work.
  3. Ensure consistency in file organization.

## ------------- Features --------------

- **Automatic Folder Creation**: The script creates necessary folders if they do not already exist.
- **File Categorization**: Files are moved into folders based on their extensions.
- **Customizable**: You can customize the folder names and the file extensions they handle.

## ------------ Requirements ----------

- **Python 3.6 or higher**

No external dependencies are required for this script.

## ------------ Usage -------------

1. **Define the Directory**: Specify the path to the directory you want to organize by updating the `directory_to_organize` variable.
2. **Customize Folders and Extensions**: Modify the `file_categories` dictionary to include any additional file types and corresponding folders you need.
3. **Run the Script**: Execute the script to automatically organize your files.

## ----------- How to Use --------

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/file-organizer.git
    cd file-organizer
    ```

2. **Update the Script**:
    - Open `organize_files.py` and update the `directory_to_organize` variable with the path to your directory.
    - Customize the `file_categories` dictionary if needed.

3. **Run the Script**:
    ```bash
    python organize_files.py
    ```

## ------------ Customization -------------

  1. Change the Source Directory: Update the directory_to_organize variable to the path of your directory.
  2. Add New File Types and Folders: Modify the file_categories dictionary to include additional file types and their corresponding folders.
