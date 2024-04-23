# FileToolkit

FileToolkit is a collection of Python scripts designed to streamline various file-related tasks. Whether you need to organize, analyze, merge, or search files, this toolkit offers efficient solutions to simplify your workflow.

1. **DocMergePro**
2. **FileCategorizer**
3. **FileInspector**
4. **fileTree**
5. **WordFinder**

## 1 DocMergePro

DocMergePro is a Python tool for merging documents, including PDFs, Word files, and Excel files, into single documents or workbooks.

### Features

- Merge multiple PDF files into a single PDF document.
- Merge multiple Word files into a single Word document.
- Merge multiple Excel files into a single Excel workbook.

Follow the on-screen menu to choose the type of files to merge and provide the necessary file paths.

### Dependencies

- PyPDF2
- python-docx
- openpyxl

### Usage Example

Welcome to DocMergePro - Your Document Merging Tool!

Menu:

1. Merge PDF Files
2. Merge Word Files
3. Merge Excel Files
4. Quit

Enter your choice (1/2/3/4): 1

Enter the paths of the PDF files to merge (comma-separated): /path/to/file1.pdf,/path/to/file2.pdf
Enter the path for the merged PDF output file: /path/to/merged_file.pdf

PDF files merged into '/path/to/merged_file.pdf'

## 2 FileCategorizer

FileCategorizer is a Python script for organizing files into folders based on their file extensions.

### Features

- Organize files into folders based on file extensions.
- Utilizes a graphical user interface (GUI) dialog to select the source directory.

### Usage

1. Run the script:


2. Follow the on-screen instructions to select the source directory.

3. The script will organize the files in the selected directory into subfolders based on their file extensions.

### Dependencies

- tkinter (Python's standard GUI library)

## 3 FileInspector

FileInspector is a Python script for analyzing files and folders within a specified directory.

### Features

- Count the number of files and folders.
- Visualize the distribution of file extensions.
- Visualize the distribution of file sizes.
- Search for files containing a specific keyword.
- Export analysis results to a CSV file.

### Usage

1. Run the script:


2. Follow the on-screen prompts to specify the folder to analyze and any filtering criteria.

3. The script will display analysis results and provide options to export them to a CSV file if desired.

### Dependencies

- matplotlib (for data visualization)
- datetime (for date and time manipulation)
- csv (for CSV file handling)

## 4 fileTree

fileTree is a Python script for printing the directory tree structure.

### Features

- Prints the directory tree structure with colorful formatting.

### Usage

1. Run the script:


2. Enter the root directory when prompted.

3. The script will print the directory tree structure.

### Dependencies

- colorama (for colorful output in the terminal)

## 5 WordFinder

WordFinder is a Python script for searching for a specific word or line within files in a directory.

### Features

- Search for a word or line within files recursively in a specified directory.
- Optionally replace the searched word with another word.

### Usage

1. Run the script:


2. Enter the root directory path and the word or line to search for when prompted.

3. The script will display search results and provide options to replace the searched word if desired.
