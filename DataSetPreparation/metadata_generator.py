import os
import json
import random

# Path to the directories containing the files
directory_paths = {
    './dataset/Celeb-DF/real': 588,
    './dataset/Celeb-DF/fake': 580,
    './dataset/DFDC/real': 1726,
    './dataset/DFDC/fake': 1565,
    './dataset/FF++/fake': 996,
    './dataset/FF++/real': 993
}

# Initialize an empty dictionary to store the data
file_data = {}

# Iterate over all directories and split files accordingly
for directory_path, total_files in directory_paths.items():
    # Get a shuffled list of all files in the directory
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    random.shuffle(files)

    # Determine the split point (80% train, 20% test)
    split_point = int(0.7 * total_files)
    train_files = set(files[:split_point])
    test_files = set(files[split_point:])

    # Assign files to train/test split
    for file_name in files:
        split = 'train' if file_name in train_files else 'test'
        label = 'REAL' if 'real' in directory_path else 'FAKE'

        # Construct the JSON structure for the current file
        file_data[file_name] = {
            "label": label,
            "split": split,
        }

# Output JSON file path
output_path = 'file_data.json'

# Write the dictionary to a JSON file
with open(output_path, 'w') as json_file:
    json.dump(file_data, json_file, indent=4)

print(f"JSON file has been created at {output_path}")