import os
import fnmatch
from colorama import Fore, Style

def search_word_in_files(root_dir, word_to_search):
    replacement_word = None
    replace_confirmation = False
    total_matches = 0

    while True:
        results = []
        for root, _, files in os.walk(root_dir):
            for filename in fnmatch.filter(files, '*'):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        lines = file.readlines()
                        for line_number, line in enumerate(lines, start=1):
                            if word_to_search in line:
                                result = {
                                    "File Name": filename,
                                    "File Path": file_path,
                                    "Line Number": line_number,
                                    "Matched Line": line.strip(),
                                }
                                results.append(result)
                                total_matches += 1
                                if replace_confirmation:
                                    lines[line_number - 1] = line.replace(word_to_search, replacement_word)
                                    with open(file_path, 'w', encoding='utf-8') as modified_file:
                                        modified_file.writelines(lines)
                                        print(f"Replaced '{word_to_search}' with '{replacement_word}' in {file_path}")

                except Exception as e:
                    print(f"Error reading {file_path}: {str(e)}")

        print("\nSearch Results:")
        if results:
            for result in results:
                print(Fore.CYAN + "File Name:" + Style.RESET_ALL)
                print(result["File Name"])
                print(Fore.CYAN + "File Path:" + Style.RESET_ALL)
                print(result["File Path"])
                print(Fore.CYAN + "Line Number:" + Style.RESET_ALL)
                print(result["Line Number"])
                print(Fore.CYAN + "Matched Line:" + Style.RESET_ALL)
                print(result["Matched Line"])
                print("-" * 50)
        else:
            print(Fore.YELLOW + "No matches found." + Style.RESET_ALL)

        print(Fore.GREEN + f"Total Matches Found: {total_matches}" + Style.RESET_ALL)

        action = input("\nOptions:\n1. Continue Searching\n2. Replace\n3. Exit\nChoose an option (1/2/3): ")
        if action == "1":
            word_to_search = input("Enter the word or line to search for: ")
        elif action == "2":
            replacement_word = input("Enter the replacement word: ")
            confirmation = input(f"Replace '{word_to_search}' with '{replacement_word}' in all files? (yes/no): ").strip().lower()
            if confirmation == "yes":
                replace_confirmation = True
        elif action == "3":
            break

if __name__ == "__main__":
    root_directory = input("Enter the root directory path: ")
    word_to_search = input("Enter the word or line to search for: ")
    search_word_in_files(root_directory, word_to_search)
