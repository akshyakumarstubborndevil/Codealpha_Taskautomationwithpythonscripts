import os
import shutil

source_folder = "source"
destination_folder = "destination"

files = os.listdir(source_folder)

print(files)

for file in files:
    if file.endswith(".jpg"):

        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

        print(f"{file} moved successfully")