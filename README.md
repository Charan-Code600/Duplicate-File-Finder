




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


