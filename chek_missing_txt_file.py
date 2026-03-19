import os

def check_images_and_labels(folder_path):
    missing_txt = []

    for root, dirs, files in os.walk(folder_path):
        files_set = set(files)  # for faster lookup

        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                base_name = os.path.splitext(file)[0]
                txt_file = base_name + ".txt"

                if txt_file not in files_set:
                    missing_txt.append(os.path.join(root, file))

    return missing_txt


def delete_images_without_labels(folder_path):
    deleted_files = []

    for root, dirs, files in os.walk(folder_path):
        files_set = set(files)

        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                base_name = os.path.splitext(file)[0]
                txt_file = base_name + ".txt"

                if txt_file not in files_set:
                    image_path = os.path.join(root, file)
                    
                    # Delete the image
                    os.remove(image_path)
                    deleted_files.append(image_path)

    return deleted_files

# Usage
folder_path = "./Data/all_images"
#------------------------------------------------
missing_files = check_images_and_labels(folder_path)
if missing_files:
    print("Images without corresponding .txt files:\n")
    for f in missing_files:
        print(f)
else:
    print("All images have corresponding .txt files ✅")
    
# -------------------------------------------------------------
deleted = delete_images_without_labels(folder_path)

print(f"Deleted {len(deleted)} files:\n")
for f in deleted:
    print(f)