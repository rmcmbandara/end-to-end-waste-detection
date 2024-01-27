

import os

source_folder = "C:\\Users\\rcmba\\end-to-end-waste-detection\\CCTV\\jpeg"  # Replace with the actual folder path

for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpeg"):
        old_filepath = os.path.join(source_folder, filename)
        new_filename = filename[:-5] + ".jpg"  # Replace .jpeg with .jpg
        new_filepath = os.path.join(source_folder, new_filename)

        try:
            os.rename(old_filepath, new_filepath)
            print(f"Renamed {filename} to {new_filename}")
        except FileExistsError:
            print(f"Skipping {filename} as {new_filename} already exists.")
        except OSError as e:
            print(f"Error renaming {filename}: {e}")

print("Renaming complete!")
