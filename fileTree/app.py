import os
from colorama import Fore, Style, init

init(autoreset=True)

def print_tree(directory, indent=""):
    try:
        items = os.listdir(directory)
    except OSError:
        return

    items.sort()

    for i, item in enumerate(items):
        path = os.path.join(directory, item)
        is_last = i == len(items) - 1

        if os.path.isdir(path):
            if is_last:
                print(indent + Fore.LIGHTGREEN_EX + "└── " + item + Style.RESET_ALL)
                print_tree(path, indent + "    ")
            else:
                print(indent + Fore.LIGHTGREEN_EX + "├── " + item + Style.RESET_ALL)
                print_tree(path, indent + "│   ")
        else:
            if is_last:
                print(indent + Fore.LIGHTWHITE_EX + "└── " + item + Style.RESET_ALL)
            else:
                print(indent + Fore.LIGHTWHITE_EX + "├── " + item + Style.RESET_ALL)

if __name__ == "__main__":
    root_directory = input("Enter the root directory: ")
    print_tree(root_directory)
