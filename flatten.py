import os
import argparse

SYSTEMINSTRUCTIONS = """
## System Instructions for Language Model Assistance in Code Debugging

### Role Definition:
- **Act as a software engineer** tasked with assisting in debugging code.
- Provide insights, explanations, and solutions based on the provided codebase information.

### Codebase Markdown File Structure:
- The codebase markdown file represents the actual codebase structure and content.
- It begins with a directory tree representation:
```
### DIRECTORY path/to/file/tree FOLDER STRUCTURE ###
(file tree representation)
### DIRECTORY path/to/file/tree FOLDER STRUCTURE ###
```
- Following the directory tree, the contents of each file are displayed:
```
### path/to/file1 BEGIN ###
(content of file1)
### path/to/file1 END ###

### path/to/file2 BEGIN ###
(content of file2)
### path/to/file2 END ###
```

### Guidelines for Interaction:
- Respond to queries based on the explicit content provided within the markdown file.
- Avoid making assumptions about the code without clear evidence presented in the file content.
- When seeking specific implementation details, refer to the corresponding section in the markdown file, for example:
```
### folder1/folder2/myfile.ts BEGIN ###
(specific implementation details)
### folder1/folder2/myfile.ts END ###
```

### Objective:
- The primary objective is to facilitate effective debugging by providing accurate information and guidance strictly adhering to the content available in the markdown file.
"""

def printFolderStructure(directory, output_file, ignore_dirs):
    """
    Print the folder structure of a directory, ignoring specified directories.
    """
    output_file.write(f"### DIRECTORY {directory} FOLDER STRUCTURE ###\n")
    for root, directories, files in os.walk(directory):
        # Exclude ignored directories
        directories[:] = [d for d in directories if d not in ignore_dirs]
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        output_file.write('{}{}/\n'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            output_file.write('{}{}\n'.format(subindent, f))
    output_file.write(f"### DIRECTORY {directory} FOLDER STRUCTURE ###\n\n")

def walkFolderTree(folder, ignore_dirs):
    """
    Traverse the folder tree, yielding file paths while ignoring specified directories.
    """
    for dirpath, dirnames, filenames in os.walk(folder):
        # Exclude ignored directories
        dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
        for filename in filenames:
            yield os.path.join(dirpath, filename)

def main():
    """
    Main function to handle command-line arguments and process folders.
    """
    parser = argparse.ArgumentParser(description='Flattens a codebase.')
    parser.add_argument('--folders', nargs='*', required=True, help='Base folders to process')
    parser.add_argument('--ignore', nargs='*', default=[], help='Directories to ignore during processing')
    parser.add_argument('--system_instructions', action='store_true', help='Print system instructions')

    args = parser.parse_args()

    if args.system_instructions:
        print(SYSTEMINSTRUCTIONS)
        return

    base_folders = args.folders
    ignore_dirs = args.ignore

    with open('codebase.md', 'w') as output_file:
        for base_folder in base_folders:
            # Print folder structure, ignoring specified directories
            printFolderStructure(base_folder, output_file, ignore_dirs)

            # Flatten file content
            output_file.write(f"### DIRECTORY {base_folder} FLATTENED CONTENT ###\n")
            for filepath in walkFolderTree(base_folder, ignore_dirs):
                content = f"### {filepath} BEGIN ###\n"
                try:
                    with open(filepath, "r") as f:
                        content += f.read()
                    content += f"\n### {filepath} END ###\n\n"
                except Exception as e:
                    print(f"Error reading file {filepath}: {e}")
                    continue
                output_file.write(content)
            output_file.write(f"### DIRECTORY {base_folder} FLATTENED CONTENT ###\n")

if __name__ == "__main__":
    main()
