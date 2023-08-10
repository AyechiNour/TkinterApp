import os
import glob

# Root directory of your project
project_root = "C:\\Users\\Dell Pc\\Documents\\projects\\projetTkinter"

# Get a list of all Python files in the project directory and its subdirectories
python_files = glob.glob(os.path.join(project_root, '**', '*.py'), recursive=True)

# Extract module names from file paths
modules = [os.path.splitext(os.path.relpath(file, project_root))[0].replace(os.path.sep, '.')
           for file in python_files]

# Print the list of module names
for module in modules:
    print(module)
