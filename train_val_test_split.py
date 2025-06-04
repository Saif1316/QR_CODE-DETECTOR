import shutil
import os
from pathlib import Path
from sklearn.model_selection import train_test_split

# Configuration
image_dir = "C:/Users/Saif/OneDrive/Pictures/Desktop/Pixonates lab Internship project/images-qr-detect/images"
label_dir = "C:/Users/Saif/OneDrive/Pictures/Desktop/YOLO_Format"
dataset_dir = "C:/Users/Saif/OneDrive/Pictures/Desktop/Pixonates lab Internship project/data"
image_extension = ".jpg"

train_ratio = 0.70
val_ratio = 0.15
test_ratio = 0.15

# Validate ratios
if abs(train_ratio + val_ratio + test_ratio - 1.0) > 1e-6:
    raise ValueError("Split ratios must sum to 1")

# Verify directories
if not Path(image_dir).exists():
    print(f"Error: image_dir {image_dir} does not exist")
    exit(1)
if not Path(label_dir).exists():
    print(f"Error: label_dir {label_dir} does not exist")
    exit(1)

# Create subdirectories
for split in ['train', 'val', 'test']:
    img_dir = Path(dataset_dir) / "Images" / split
    lbl_dir = Path(dataset_dir) / "Labels" / split
    try:
        img_dir.mkdir(parents=True, exist_ok=True)
        lbl_dir.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {img_dir}")
        print(f"Created directory: {lbl_dir}")
    except Exception as e:
        print(f"Error creating directory {img_dir} or {lbl_dir}: {e}")
        exit(1)

# Get images
images = list(Path(image_dir).glob(f"*{image_extension}"))
if len(images) != 80:
    print(f"Warning: Found {len(images)} images, expected 80")
if not images:
    print(f"Error: No images found in {image_dir}")
    exit(1)

# Convert Path objects to strings
image_paths = [str(img) for img in images]

# Split dataset
train_paths, val_test_paths = train_test_split(
    image_paths,
    test_size=(val_ratio + test_ratio),
    random_state=42,
    shuffle=True
)
val_paths, test_paths = train_test_split(
    val_test_paths,
    test_size=test_ratio / (val_ratio + test_ratio),
    random_state=42,
    shuffle=True
)

# Map splits
splits = {
    "train": train_paths,
    "val": val_paths,
    "test": test_paths
}

# Copy files
for split, path_list in splits.items():
    img_split_dir = Path(dataset_dir) / "Images" / split
    lbl_split_dir = Path(dataset_dir) / "Labels" / split
    copied_images = 0
    copied_labels = 0
    for img_path in path_list:
        img = Path(img_path)
        if not img.exists():
            print(f"Warning: Image {img} does not exist, skipping")
            continue
        try:
            shutil.copy(img, img_split_dir / img.name)
            copied_images += 1
        except Exception as e:
            print(f"Error copying image {img} to {img_split_dir / img.name}: {e}")
            continue
        lbl = Path(label_dir) / (img.stem + ".txt")
        if lbl.exists() and os.path.getsize(lbl) > 0:
            try:
                shutil.copy(lbl, lbl_split_dir / lbl.name)
                copied_labels += 1
            except Exception as e:
                print(f"Error copying label {lbl} to {lbl_split_dir / lbl.name}: {e}")
                continue
        else:
            print(f"Warning: Label {lbl} missing or empty for {img.name}")
    print(f"Copied {copied_images} images and {copied_labels} labels to {split}")

print(f"Dataset split complete: {len(train_paths)} train, {len(val_paths)} val, {len(test_paths)} test")