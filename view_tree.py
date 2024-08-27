import os


def display_folder_structure(root_dir, indent=0):
    # List all the items in the directory, ignoring .git
    items = [item for item in os.listdir(root_dir) if item != ".git"]

    # Iterate over each item in the directory
    for item in sorted(items):
        item_path = os.path.join(root_dir, item)
        # Print the item with indentation based on its level in the folder structure
        print("  " * indent + "|-- " + item)

        # If the item is a directory, recursively display its structure
        if os.path.isdir(item_path):
            display_folder_structure(item_path, indent + 1)


# Get the current working directory
root_directory = os.getcwd()

# Display the folder structure starting from the current directory
display_folder_structure(root_directory)
