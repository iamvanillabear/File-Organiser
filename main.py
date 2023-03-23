import os
import shutil

# Define the directory to organize
directory = "/path/to/directory"

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Get the file extension
    extension = os.path.splitext(filename)[1][1:].lower()

    # Skip directories and files that have no extension
    if os.path.isdir(os.path.join(directory, filename)) or not extension:
        continue

    # Create a directory for the extension if it doesn't exist
    if not os.path.exists(os.path.join(directory, extension)):
        os.makedirs(os.path.join(directory, extension))

    # Move the file into the directory for the extension
    shutil.move(os.path.join(directory, filename), os.path.join(directory, extension, filename))
