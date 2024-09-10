import os
import hashlib
import time

# Function to hash a file
def hash_file(filename):
    hasher = hashlib.sha256()
    with open(filename, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()

# Function to get all files in a directory
def get_all_files_in_directory(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

# Function to create a baseline and erase the old one if it exists
def create_baseline(directory, baseline_file='baseline.txt'):
    if os.path.exists(baseline_file):
        os.remove(baseline_file)  # Remove the old baseline

    files = get_all_files_in_directory(directory)
    with open(baseline_file, 'w') as f:
        for file in files:
            if os.path.isfile(file):
                file_hash = hash_file(file)
                f.write(f'{file},{file_hash}\n')
                print(f'Baseline created for {file}')
            else:
                print(f'{file} does not exist, skipping.')

# Function to load the baseline
def load_baseline(baseline_file='baseline.txt'):
    baseline = {}
    if os.path.exists(baseline_file):
        with open(baseline_file, 'r') as f:
            for line in f:
                file, file_hash = line.strip().split(',')
                baseline[file] = file_hash
    else:
        print(f'{baseline_file} not found.')
    return baseline

# Function to monitor files based on the baseline
def monitor_files(baseline):
    while True:
        for file, old_hash in baseline.items():
            if os.path.isfile(file):
                new_hash = hash_file(file)
                if new_hash != old_hash:
                    print(f'{file} has changed!')
            else:
                print(f'{file} has been deleted!')
        time.sleep(10)  # Check every 10 seconds

def main():
    choice = input("Enter 'A' to create a new baseline or 'B' to monitor files using the saved baseline: ").strip().upper()
    

    if choice == 'A':
        directory = input("Enter the directory path to monitor: ").strip()

        if not os.path.isdir(directory):
            print(f"{directory} is not a valid directory.")
            return
        create_baseline(directory)
    elif choice == 'B':
        directory = input("Enter the directory path to monitor: ").strip()

        if not os.path.isdir(directory):
            print(f"{directory} is not a valid directory.")
            return
        baseline = load_baseline()
        if baseline:
            monitor_files(baseline)
        else:
            print("No valid baseline to monitor.")
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
