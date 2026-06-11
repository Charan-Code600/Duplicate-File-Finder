




import os

print("""
====================
Duplicate File Finder
====================
""")

folder = input("Enter folder path: ")

if not os.path.exists(folder):
    print("❌ Folder not found!")
else:
    files = os.listdir(folder)
    seen = {}
    duplicates = []

    for file in files:
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            if file_size in seen:
                duplicates.append(file)
            else:
                seen[file_size] = file

    if len(duplicates) == 0:
        print("✅ No duplicates found!")
    else:
        print(f"\n⚠️ Found {len(duplicates)} duplicate(s)!")
        for d in duplicates:
            print(f"  → {d}")

        choice = input("\nDelete duplicates? (yes/no): ")
        if choice == "yes":
            for d in duplicates:
                os.remove(os.path.join(folder, d))
            print("✅ Duplicates deleted!")
        else:
            print("👋 Bye!")




            
