import os
import shutil

def collect_images(source_folder, destination_folder):
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Walk through all subfolders
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # Check for .jpg files (case insensitive)
            if file.lower().endswith(".jpg"):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)

                # Handle duplicate filenames
                base, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(destination_path):
                    new_name = f"{base}_{counter}{ext}"
                    destination_path = os.path.join(destination_folder, new_name)
                    counter += 1

                # Copy file
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {source_path} -> {destination_path}")

# Example usage
source_folder = "./CollectedImages"
destination_folder = "./all_images"

collect_images(source_folder, destination_folder)
