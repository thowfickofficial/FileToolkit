import os
import shutil
import mimetypes
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pyfiglet

# Function to organize files into folders based on file extensions
def organize_files(source_dir):
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        # Check if it's a file
        if os.path.isfile(file_path):
            # Get the file extension (including the dot)
            file_ext = os.path.splitext(filename)[1].lower()

            # Determine the destination folder based on the file extension
            destination_folder = file_ext[1:] if file_ext else 'Other'

            # Create the destination folder if it doesn't exist
            destination_dir = os.path.join(source_dir, destination_folder)
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)

            # Move the file to the destination folder
            shutil.move(file_path, os.path.join(destination_dir, filename))

# Function to get the source directory using a GUI dialog
def get_source_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    source_directory = filedialog.askdirectory(
        title="Select the source directory",
        initialdir=os.path.expanduser("~"),
    )
    
    return source_directory

if __name__ == "__main__":
    # Generate ASCII art for the tool's name
    tool_name = "FileCategorizer"
    ascii_art = pyfiglet.figlet_format(tool_name, font="slant")
    print(ascii_art)

    print("Welcome to the FileCategorizer!")
    print("This tool will organize your files into folders based on file extensions.")
    
    # Get the source directory from the user using a GUI dialog
    source_directory = get_source_directory()
    
    if source_directory:
        print(f"Organizing files in {source_directory}...")
        
        # Organize the files based on file extensions
        organize_files(source_directory)
        
        messagebox.showinfo("Success", "Files organized successfully!")
    else:
        messagebox.showwarning("No Directory Selected", "No source directory selected. Please try again.")
