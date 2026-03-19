import os
import shutil
import random
from collections import defaultdict

def stratified_split(source_folder, destination_folder, split_ratio=0.8):
    class_data = defaultdict(list)

    # Step 1: Group by class
    for file in os.listdir(source_folder):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            base_name = os.path.splitext(file)[0]
            txt_file = base_name + ".txt"

            image_path = os.path.join(source_folder, file)
            txt_path = os.path.join(source_folder, txt_file)

            if os.path.exists(txt_path):
                class_name = base_name.split(".")[0]  # "Hello.xxx" → "Hello"
                class_data[class_name].append((image_path, txt_path))

    # Step 2: Create folders
    paths = [
        "train/images", "train/labels",
        "test/images", "test/labels"
    ]

    for path in paths:
        os.makedirs(os.path.join(destination_folder, path), exist_ok=True)

    # Step 3: Split per class
    for class_name, items in class_data.items():
        random.shuffle(items)

        split_index = int(len(items) * split_ratio)
        train_items = items[:split_index]
        test_items = items[split_index:]

        print(f"{class_name} → Train: {len(train_items)}, Test: {len(test_items)}")

        # Copy function
        def copy_data(data, folder_type):
            for img_path, txt_path in data:
                shutil.copy2(img_path, os.path.join(destination_folder, f"{folder_type}/images", os.path.basename(img_path)))
                shutil.copy2(txt_path, os.path.join(destination_folder, f"{folder_type}/labels", os.path.basename(txt_path)))

        copy_data(train_items, "train")
        copy_data(test_items, "test")


# 🔹 Usage
source_folder = "./Data/all_images"
destination_folder = "./Data/final_data"

random.seed(42)  # optional (for reproducibility)

stratified_split(source_folder, destination_folder)