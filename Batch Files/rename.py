import os
import uuid

source_path = "C:\\Users\\rcmba\\end-to-end-waste-detection\\CCTV"  # Replace with your actual source path

for filename in os.listdir(source_path):
    if filename.endswith(".jpg"):
        old_filepath = os.path.join(source_path, filename)
        new_filename = str(uuid.uuid4()) + ".jpg"
        new_filepath = os.path.join(source_path, new_filename)
        os.rename(old_filepath, new_filepath)

print("JPG files renamed successfully!")