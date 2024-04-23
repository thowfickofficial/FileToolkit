import os
import csv
import matplotlib.pyplot as plt
from datetime import datetime

def count_files_and_folders(folder_path, include_subdirectories=False, min_file_size=None, min_modified_date=None):
    extension_counts = {}
    folder_count = 0
    file_sizes = {}
    
    for root, dirs, files in os.walk(folder_path):
        if not include_subdirectories and root != folder_path:
            continue
        
        for file in files:
            _, file_ext = os.path.splitext(file)
            file_ext = file_ext.lower()
            
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_modified = os.path.getmtime(file_path)
            
            if min_file_size is not None and file_size < min_file_size:
                continue
            
            if min_modified_date is not None and file_modified < min_modified_date:
                continue
            
            if file_ext not in extension_counts:
                extension_counts[file_ext] = 1
            else:
                extension_counts[file_ext] += 1
            
            if file_ext in file_sizes:
                file_sizes[file_ext] += file_size
            else:
                file_sizes[file_ext] = file_size
        
        folder_count += len(dirs)
    
    return extension_counts, folder_count, file_sizes

def visualize_extension_distribution(extension_counts):
    extensions = list(extension_counts.keys())
    counts = list(extension_counts.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(extensions, counts)
    plt.xlabel("File Extensions")
    plt.ylabel("File Counts")
    plt.title("Distribution of File Extensions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualize_file_size_distribution(file_sizes):
    sizes = list(file_sizes.values())
    
    plt.figure(figsize=(10, 6))
    plt.hist(sizes, bins=20, edgecolor='black')
    plt.xlabel("File Sizes (bytes)")
    plt.ylabel("Number of Files")
    plt.title("Distribution of File Sizes")
    plt.tight_layout()
    plt.show()

def search_files_by_keyword(folder_path, keyword):
    matching_files = []
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            if keyword.lower() in file.lower():
                matching_files.append(os.path.join(root, file))
    
    return matching_files

def export_to_csv(extension_counts, csv_filename):
    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Extension', 'File Count'])
        for ext, count in extension_counts.items():
            writer.writerow([ext, count])

def main():
    print("File and Folder Analyzer")
    print("------------------------")
    
    folder_path = input("Enter the full path to the folder you want to analyze: ")
    include_subdirectories = input("Include subdirectories? (y/n): ").lower() == "y"
    min_file_size = int(input("Enter the minimum file size (bytes) or leave empty for no filter: ") or "0")
    min_modified_date_str = input("Enter the minimum modified date (YYYY-MM-DD) or leave empty for no filter: ")
    min_modified_date = None
    if min_modified_date_str:
        min_modified_date = datetime.strptime(min_modified_date_str, "%Y-%m-%d").timestamp()
    
    if os.path.exists(folder_path):
        extension_counts, folder_count, file_sizes = count_files_and_folders(
            folder_path, include_subdirectories, min_file_size, min_modified_date)
        
        print("\nFile Extension Counts:")
        for ext, count in extension_counts.items():
            print(f"*.{ext}: {count} file(s)")
        
        print(f"\nTotal Folders: {folder_count}")
        
        print("\nFile Size Distribution:")
        for ext, size in file_sizes.items():
            print(f"*.{ext}: Total size {size} bytes")
        
        visualize_extension_distribution(extension_counts)
        visualize_file_size_distribution(file_sizes)
        
        keyword_search = input("\nEnter keyword to search for files (leave empty to skip): ")
        if keyword_search:
            matching_files = search_files_by_keyword(folder_path, keyword_search)
            if matching_files:
                print("\nMatching Files:")
                for file in matching_files:
                    print(file)
            else:
                print("\nNo matching files found.")
        
        export_csv_option = input("\nExport results to CSV? (y/n): ").lower()
        if export_csv_option == "y":
            csv_filename = input("Enter the CSV file name: ")
            export_to_csv(extension_counts, csv_filename)
            print(f"Results exported to '{csv_filename}'.")
        
    else:
        print("Folder path does not exist.")

if __name__ == "__main__":
    main()
