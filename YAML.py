from pathlib import Path

# Configuration
dataset_dir = "C:/Users/Saif/OneDrive/Pictures/Desktop/Pixonates lab Internship project/data"
yaml_path = Path(dataset_dir) / "data.yaml"

# YAML content
yaml_content = """path: ./
train: Images/train
val: Images/val
test: Images/test
names:
  0: qr_code
  1: Other
"""

# Write YAML file
try:
    with open(yaml_path, "w") as f:
        f.write(yaml_content)
    print(f"Created {yaml_path}")
except Exception as e:
    print(f"Error creating {yaml_path}: {e}")