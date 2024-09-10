# File Integrity Monitor

This is a simple Python-based file integrity monitor that allows users to create a baseline of file hashes for a specified folder and then continuously monitor that folder for any changes to the files. The program notifies users if any files are modified, added, or deleted.

## Features:
- Create a baseline of file hashes for all files in a specified folder.
- Continuously monitor files for changes based on the baseline.
- Automatically deletes and replaces the old baseline when creating a new one.

## How to Install:

1. **Clone the Repository:**
   Open your terminal and run the following command to clone the repository to your local machine:

   ```bash
   git clone https://github.com/Tala1122/FileIntegrityMonitor.git
2. **Navigate to the Project Directory:**
   ```bash
   cd FileIntegrityMonitor
## How to Use
**Run the program**
   ```bash
   python3 fim.py
```
   
The program will ask whether you want to:
- Create a new baseline (Option A)
- Monitor files using a previously saved baseline (Option B)
After selecting an option, you will be prompted to enter the path to the directory you want to monitor. For example, to monitor a folder named example on your Desktop, enter:
```bash
 /Users/your-username/Desktop/example
```
**Create a New Baseline**: If you choose option "A", the program will generate file hashes for all files in the specified folder and save them in baseline.txt. If a previous baseline exists, it will be replaced.

**Monitor Files**: If you choose option "B", the program will load the saved baseline from baseline.txt and continuously monitor the folder for any changes (modifications, deletions, or additions).
