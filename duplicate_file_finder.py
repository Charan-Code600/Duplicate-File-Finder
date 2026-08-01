




import os
import hashlib


print("""

*******************************************************
        ╔══════════════════════════════════╗
        ║     DUPLICATE FILE FINDER        ║
        ╚══════════════════════════════════╝
*******************************************************

""")


def get_file_hash(filepath):
    """Returns SHA-256 hash of a file's content, or None if it can't be read."""
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as file:
            while chunk := file.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        print(f"⚠️  Could not read: {filepath} ({e})")
        return None


folder = input("Enter folder path: ").strip()

if not os.path.isdir(folder):
    print("❌ Error: Folder not found!")
    exit()

print("\n🔍 Scanning files...")
all_files = []
for root, dirs, files in os.walk(folder):
    for file in files:
        all_files.append(os.path.join(root, file))

print(f"📁 Total files found: {len(all_files)}")

hash_dict = {}
skipped_empty = 0

for filepath in all_files:
    if os.path.getsize(filepath) == 0:
        skipped_empty += 1
        continue

    file_hash = get_file_hash(filepath)
    if file_hash:
        hash_dict.setdefault(file_hash, []).append(filepath)

if skipped_empty:
    print(f"ℹ️  Skipped {skipped_empty} empty (0-byte) file(s) — not treated as duplicates.")

duplicates = {h: files for h, files in hash_dict.items() if len(files) > 1}

if not duplicates:
    print("\n✅ No duplicate files found.")
    exit()

print("\n" + "=" * 50)
print("Duplicate Files Found:")
print("=" * 50)

group_no = 1
files_to_delete = []

for files in duplicates.values():
    sorted_files = sorted(files, key=os.path.getmtime)
    keep_file = sorted_files[0]
    delete_files = sorted_files[1:]

    print(f"\nGroup {group_no}:")
    print(f"  ✅ KEEP   : {keep_file}")
    for f in delete_files:
        print(f"  🗑️  DELETE : {f}")

    files_to_delete.extend(delete_files)
    group_no += 1

print("\n" + "-" * 50)
print(f"Duplicate groups found : {len(duplicates)}")
print(f"Files that will be deleted : {len(files_to_delete)}")
print("(The oldest file in each group is always kept.)")
print("-" * 50)

choice = input("\nDelete these duplicate files? (yes/no): ").strip().lower()

if choice in ("y", "yes"):
    deleted = 0
    for file in files_to_delete:
        try:
            os.remove(file)
            deleted += 1
        except Exception as e:
            print(f"❌ Delete failed: {file} ({e})")
    print(f"\n✅ Deleted {deleted} file(s).")
else:
    print("\n❌ No files deleted.")

    










