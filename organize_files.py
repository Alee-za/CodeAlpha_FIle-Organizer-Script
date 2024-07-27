import os
import shutil

# Define the directory to organize
directory_to_organize = 'path_to_your_directory'

# Define the destination folders for different file types
file_categories = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.tar.gz'],
    'CodeFiles': ['.py', '.js', '.html', '.css']
}

def create_folders(base_dir, categories):
    """Create folders if they don't already exist."""
    for folder in categories:
        folder_path = os.path.join(base_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def move_files(base_dir, categories):
    """Move files to their respective folders based on file extensions."""
    for file in os.listdir(base_dir):
        file_path = os.path.join(base_dir, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            for folder, extensions in categories.items():
                if file_ext in extensions:
                    destination_folder = os.path.join(base_dir, folder)
                    shutil.move(file_path, destination_folder)
                    print(f'Moved {file} to {folder}')
                    break

def main():
    create_folders(directory_to_organize, file_categories)
    move_files(directory_to_organize, file_categories)
    print('File organization complete.')

if __name__ == '__main__':
    main()
