




<!-- ==================== ANIMATED BANNER ==================== -->


<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=cylinder&color=0:0f2027,100:2c5364&height=160&section=header&text=Duplicate%20File%20Finder&fontSize=44&fontColor=FFB800&animation=scaleIn&fontAlignY=42&desc=Python%20%7C%20SHA-256%20%7C%20File%20Handling&descSize=18&descAlignY=68" width="100%"/>
</div>


<!-- ==================== Tagline ==================== -->

<div align="center">

### A command-line tool that scans a folder and all its subfolders, finds duplicate files by comparing their actual content with SHA-256 hashing, and deletes the extra copies only after you confirm.

</div>


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>


<!-- ==================== Open to Freelance Work ==================== -->

<p align="center">
    <img src="https://img.shields.io/badge/Status-Open%20to%20Freelance%20Work-brightgreen?style=for-the-badge&labelColor=1a1a2e" />
</p>


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>


<!-- ==================== Badges ==================== -->

<div align="center">

# $\textsf{\color{#FFB800}{Badges}}$

</div>

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-None-00C851?style=for-the-badge)
![Interface](https://img.shields.io/badge/Interface-CLI-2B2B2B?style=for-the-badge&logo=gnubash&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-FFB800?style=for-the-badge)

</div>

<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>




<!-- ==================== Table of Contents ==================== -->

<div align="center">

#  $\textsf{\color{#FFB800}{Table of Contents}}$

</div>

<div align="center">
<table>
<tr><td align="left">

[![1 Overview](https://img.shields.io/badge/1-Overview-FFB800?style=for-the-badge&labelColor=1a1a2e)](#overview)
<br>
[![2 Demo](https://img.shields.io/badge/2-Demo-FFB800?style=for-the-badge&labelColor=1a1a2e)](#demo)
<br>
[![3 Features](https://img.shields.io/badge/3-Features-FFB800?style=for-the-badge&labelColor=1a1a2e)](#features)
<br>
[![4 Tech Stack](https://img.shields.io/badge/4-Tech%20Stack-FFB800?style=for-the-badge&labelColor=1a1a2e)](#tech-stack)
<br>
[![5 Installation](https://img.shields.io/badge/5-Installation-FFB800?style=for-the-badge&labelColor=1a1a2e)](#installation)
<br>
[![6 How to Use](https://img.shields.io/badge/6-How%20to%20Use-FFB800?style=for-the-badge&labelColor=1a1a2e)](#how-to-use)
<br>
[![7 Project Structure](https://img.shields.io/badge/7-Project%20Structure-FFB800?style=for-the-badge&labelColor=1a1a2e)](#project-structure)
<br>
[![8 Key Highlights](https://img.shields.io/badge/8-Key%20Highlights-FFB800?style=for-the-badge&labelColor=1a1a2e)](#key-highlights)
<br>
[![9 Future Improvements](https://img.shields.io/badge/9-Future%20Improvements-FFB800?style=for-the-badge&labelColor=1a1a2e)](#future-improvements)
<br>
[![10 Author](https://img.shields.io/badge/10-Author-FFB800?style=for-the-badge&labelColor=1a1a2e)](#author)

</td></tr>
</table>
</div>


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>


<!-- ==================== Overview ==================== -->

<a id="overview"></a>

![1 Overview](https://img.shields.io/badge/1-Overview-FFB800?style=for-the-badge&labelColor=1a1a2e)

<div align="center">

### Over time the same file gets copied into many folders and quietly wastes storage. Checking by hand is slow, and comparing file names is not reliable, because two files can have different names and the same content. This project scans a folder and every subfolder, creates a SHA-256 hash of each file's content, and groups the files that are identical. In each group it keeps the oldest file and, only after you confirm, deletes the rest. It was built to practise hashing, folder traversal and safe file deletion.


</div>

<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>


<!-- ==================== Demo ==================== -->

<a id="demo"></a>

![2 Demo](https://img.shields.io/badge/2-Demo-FFB800?style=for-the-badge&labelColor=1a1a2e)




<div align="center">
<i>Real output on a small test folder: one duplicate group is found and deleted after confirmation, then a second scan shows none left. The folder had a.txt, b.txt and sub/c.txt (same content), d.txt (different) and one empty file.</i>
</div>

```
*******************************************************
        ╔══════════════════════════════════╗
        ║     DUPLICATE FILE FINDER        ║
        ╚══════════════════════════════════╝
*******************************************************

        Scan a folder                    Enter  →  1
        Exit                             Enter  →  2

*******************************************************


Choose: 1
Enter folder path: C:\test_dup

🔍 Scanning files...
📁 Total files found: 5
ℹ️  Skipped 1 empty (0-byte) file(s) — not treated as duplicates.

==================================================
Duplicate Files Found:
==================================================

Group 1:
  ✅ KEEP   : C:\test_dup\a.txt
  🗑️  DELETE : C:\test_dup\b.txt
  🗑️  DELETE : C:\test_dup\sub\c.txt

--------------------------------------------------
Duplicate groups found : 1
Files that will be deleted : 2
(The oldest file in each group is always kept.)
--------------------------------------------------

Delete these duplicate files? (yes/no): no

❌ No files deleted.

Choose: 1
Enter folder path: C:\test_dup

🔍 Scanning files...
📁 Total files found: 5
ℹ️  Skipped 1 empty (0-byte) file(s) — not treated as duplicates.

==================================================
Duplicate Files Found:
==================================================

Group 1:
  ✅ KEEP   : C:\test_dup\a.txt
  🗑️  DELETE : C:\test_dup\b.txt
  🗑️  DELETE : C:\test_dup\sub\c.txt

--------------------------------------------------
Duplicate groups found : 1
Files that will be deleted : 2
(The oldest file in each group is always kept.)
--------------------------------------------------

Delete these duplicate files? (yes/no): yes

✅ Deleted 2 file(s).

Choose: 1
Enter folder path: C:\test_dup

🔍 Scanning files...
📁 Total files found: 3
ℹ️  Skipped 1 empty (0-byte) file(s) — not treated as duplicates.

✅ No duplicate files found.

Choose: 2

👋 Goodbye!
```


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>


<!-- ==================== Features ==================== -->

<a id="features"></a>

![3 Features](https://img.shields.io/badge/3-Features-FFB800?style=for-the-badge&labelColor=1a1a2e)

<div align="center">

| Feature | What it does |
|:--|:--|
| 🔐 **Content-based Detection** | Compares SHA-256 hashes of file content, so files with different names but the same content are still found |
| 📂 **Recursive Scan** | Scans the chosen folder and every subfolder inside it |
| 🧩 **Chunked Reading** | Reads each file in 8 KB pieces, so large files do not fill memory |
| 📁 **Grouped Results** | Lists duplicates in groups, with the file to KEEP and the files to DELETE clearly marked |
| 🗓️ **Predictable Keep Rule** | The oldest file (by last-modified time) in each group is always kept |
| 🧹 **Empty Files Skipped** | 0-byte files are ignored, because all empty files look the same but are not real duplicates |
| ✅ **Confirmation First** | Shows the full list and the count before deleting, and removes nothing unless you type `yes` |
| 🔁 **Menu-driven** | Scan as many folders as you like in one session without restarting the program |

</div>


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>

























































# 🔍 Duplicate File Finder

A Python tool that scans a folder (and all its subfolders) and finds duplicate files by comparing their actual content using SHA-256 hashing — not just file name or size.

## ⚠️ Important — Read Before Using

This tool can **permanently delete files**. Deleted files do **not** go to the Recycle Bin — they are removed directly. Always review the KEEP/DELETE list carefully before confirming deletion, and consider backing up important folders first.

## Features

- 🔁 Menu-driven — scan as many folders as you like in one session, no need to restart the program each time
- 🔍 Scans a folder and all its subfolders for duplicates
- 🔐 Uses SHA-256 hashing to compare actual file content (two files with different names but identical content are correctly detected as duplicates)
- 📁 Groups duplicate files together, clearly showing which file will be **kept** and which will be **deleted**
- 🗓️ Always keeps the **oldest** file in each duplicate group (by last-modified date) — a fixed, predictable rule, not random
- 🧹 Skips empty (0-byte) files automatically — these aren't treated as "duplicates" since many unrelated empty files can share the same hash
- ✅ Shows the full list of files to be deleted *before* asking for confirmation
- 🗑️ Optional deletion — nothing is deleted unless you explicitly confirm with `yes`
- ❌ Error handling for invalid folder paths, invalid menu options, and unreadable/locked files

## Requirements

- Python 3.x (no external libraries needed)

## How to Run

```bash
python duplicate_finder.py
```

## How to Use

1. Run the program — a menu appears with two options.
2. Choose **1** to scan a folder.
3. Enter the full folder path you want to scan (subfolders are included automatically).
4. The tool scans every file and groups any exact-content duplicates together.
5. For each group, it shows which file will be **kept** (the oldest one) and which will be **deleted**.
6. Review the list carefully, then type `yes` to delete the listed duplicates, or `no` to cancel — no files are touched unless you confirm.
7. You're returned to the menu — choose **1** again to scan another folder, or **2** to exit.

## How "Keep vs Delete" Is Decided

When duplicate copies of the same file are found, the tool always keeps the **oldest** one (earliest last-modified date) and marks the newer copies for deletion. This keeps the behavior predictable — the same duplicate set will always give the same result.

## Technologies Used

- Python
- os module
- hashlib (SHA-256)

## Author

**Charan Aade | Python Developer**



🔗 [GitHub](https://github.com/Charan-Code600)


