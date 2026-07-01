

            

import os

print("""
====================
Duplicate File Finder
====================
""")

import os
import hashlib


def get_file_hash(filepath):
    sha256 = hashlib.sha256()

    try:
        with open(filepath, "rb") as file:
            while chunk := file.read(8192):
                sha256.update(chunk)

        return sha256.hexdigest()

    except Exception as e:
        print(f"Hash error: {filepath}")
        return None


print("""
====================
Duplicate File Finder
====================
""")

folder = input("Enter folder path: ")

if not os.path.isdir(folder):
    print("Error: Folder nahi mila!")
    exit()

print("\nScanning files...")

all_files = []

for root, dirs, files in os.walk(folder):
    for file in files:
        all_files.append(os.path.join(root, file))

print(f"Total files found: {len(all_files)}")

hash_dict = {}

for filepath in all_files:
    file_hash = get_file_hash(filepath)

    if file_hash:
        hash_dict.setdefault(file_hash, []).append(filepath)

duplicates = {
    h: files
    for h, files in hash_dict.items()
    if len(files) > 1
}

if not duplicates:
    print("\nNo duplicate files found.")
    exit()

print("\nDuplicate Files Found:\n")

group_no = 1
duplicate_files = []

for files in duplicates.values():
    print(f"Group {group_no}")
    for file in files:
        print(file)
    print()

    duplicate_files.extend(files[1:])
    group_no += 1

print(f"Duplicate groups: {len(duplicates)}")
print(f"Files that can be deleted: {len(duplicate_files)}")

choice = input("\nDelete duplicate files? (y/n): ").lower()

if choice == "y":

    deleted = 0

    for file in duplicate_files:
        try:
            os.remove(file)
            deleted += 1
        except Exception as e:
            print(f"Delete failed: {file}")

    print(f"\nDeleted {deleted} files.")

else:
    print("\nNo files deleted.")














