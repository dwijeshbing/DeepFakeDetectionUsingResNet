import os
import random
import csv

# Path to the directories containing the files
directory_paths = {
    './dataset/Celeb-DF/real': 588,
    './dataset/Celeb-DF/fake': 580,
    './dataset/DFDC/real': 1726,
    './dataset/DFDC/fake': 1565,
    './dataset/FF++/fake': 996,
    './dataset/FF++/real': 993
}

# Output CSV file path
output_path = 'file_data.csv'

# Open the CSV file for writing
with open(output_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write the header
    csv_writer.writerow(["URI", "label", "split"])
    
    # Iterate over all directories and split files accordingly
    for directory_path, total_files in directory_paths.items():
        # Get a shuffled list of all files in the directory
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        random.shuffle(files)

        # Determine the split point (70% train, 30% test)
        split_point = int(0.7 * total_files)
        train_files = set(files[:split_point])
        test_files = set(files[split_point:])

        # Assign files to train/test split
        for file_name in files:
            split = 'train' if file_name in train_files else 'test'
            label = 'REAL' if 'real' in directory_path.lower() else 'FAKE'
            
            # Write the row to the CSV file
            csv_writer.writerow([file_name, label, split])

print(f"CSV file has been created at {output_path}")
