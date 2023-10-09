import os
import shutil
import sys
import subprocess

# Python version 3.11.5
# Code from ChatGPT
# Made By Bank's : Thai translator H Game
# Link Discord : https://discord.gg/q6FkGCHv66

# โปรแกรมนี้ใช้เพื่อคัดแยกไฟล์ที่ตรงกับคำค้นหาแล้วย้ายไฟล์นั้นออกมาไว้ในโฟลเดอร์ใหม่
# This program is used to extract files that match a search term and move them into a new folder.

# How to use on PC
# Just input Folder paths, and the file extension

# วิธีใช้บนคอม
# เพียงแค่ป้อนตำแหน่งของโฟลเดอร์ และนามสกุลของไฟล์นั้น ๆ 

# How to use in moblie version
# Please run in Pydroid 3 - IDE for Python 3
# Then Just input Folder paths and the file extension
# If you put flie in Pyroid3 Folder the path is [/storage/emulated/0/Documents/Pydroid3/(Put your folder name here)"]

# วิธีใช้บนมือถือ
# ให้รันบนPydroid 3 - IDE for Python 3
# ถ้าเอาไฟล์ดิบที่ต้องการไว้ในโฟลเดอร์  Pyroid3 ตำแหน่งไฟล์คือ [/storage/emulated/0/Documents/Pydroid3/(ใส่ชื่อโฟลเดอร์ตรงนี้)]
# เพียงแค่ป้อนตำแหน่งของโฟลเดอร์ และนามสกุลของไฟล์นั้น ๆ 

# Check if tqdm is installed, and if not, install it
try:
    from tqdm import tqdm
except ImportError:
    print("tqdm not found! Installing tqdm...")
    subprocess.run([sys.executable, "-m", "pip", "install", "tqdm"])
    from tqdm import tqdm

def get_valid_folder_path():
    while True:
        folder_path = input("Please enter the folder path or type 'done' to finish: ")
        if folder_path.lower() == 'done':
            if not folder_paths:
                print("No folder paths have been added yet!")
                continue
            return None
        if os.path.isdir(folder_path):
            return folder_path
        else:
            print("Invalid folder path. Please try again.")

def sanitize_folder_name(keyword):
    # List of invalid characters for folder names on Windows
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        keyword = keyword.replace(char, '')
    # If after removing invalid chars the keyword becomes empty, use a default name
    if not keyword:
        return "WithKeyword"
    return f"With Keyword ({keyword})"

print("""
Python version 3.11.5
Code from ChatGPT
Made By Bank's : Thai translator H Game
Link Discord : https://discord.gg/q6FkGCHv66

โปรแกรมนี้ใช้เพื่อคัดแยกไฟล์ที่ตรงกับคำค้นหาแล้วย้ายไฟล์นั้นออกมาไว้ในโฟลเดอร์ใหม่
This program is used to extract files that match a search term and move them into a new folder.

How to use on PC
Just input Folder paths, and the file extension

วิธีใช้บนคอม
เพียงแค่ป้อนตำแหน่งของโฟลเดอร์ และนามสกุลของไฟล์นั้น ๆ 

How to use in moblie version
Please run in Pydroid 3 - IDE for Python 3
Then Just input Folder paths and the file extension
If you put flie in Pyroid3 Folder the path is [/storage/emulated/0/Documents/Pydroid3/(Put your folder name here)"]

วิธีใช้บนมือถือ
ให้รันบนPydroid 3 - IDE for Python 3
ถ้าเอาไฟล์ดิบที่ต้องการไว้ในโฟลเดอร์  Pyroid3 ตำแหน่งไฟล์คือ [/storage/emulated/0/Documents/Pydroid3/(ใส่ชื่อโฟลเดอร์ตรงนี้)]
เพียงแค่ป้อนตำแหน่งของโฟลเดอร์ และนามสกุลของไฟล์นั้น ๆ 
"""
)

while True:
    # Get folder paths
    folder_paths = set()

    while True:
        folder_path = get_valid_folder_path()
        if folder_path is None:
            break
        if folder_path in folder_paths:
            print("This folder path has already been added.")
        else:
            folder_paths.add(folder_path)

    folder_paths = list(folder_paths)

    # Get file extension
    file_extension = input("Please enter the file extension you want to search for (e.g. .txt, .docx): ")

    # Get keyword
    keyword = input("Enter the keyword to search for: ")

    # Set up the new folder for files containing the keyword
    new_folder_name = sanitize_folder_name(keyword)
    new_folder_path = os.path.join(os.path.dirname(folder_paths[0]), new_folder_name)

    # Create the new folder if it doesn't exist
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

    files_to_search = []

    # Loop through each folder to gather files to search
    for folder_path in folder_paths:
        for filename in os.listdir(folder_path):
            if filename.endswith(file_extension):
                file_path = os.path.join(folder_path, filename)
                files_to_search.append(file_path)

    # Loop through each file in files_to_search with a progress bar
    for file_path in tqdm(files_to_search, desc="Searching files", unit="file"):
        with open(file_path, 'r', encoding='utf8') as f:
            content = f.read()

        if keyword in content:
            new_file_path = os.path.join(new_folder_path, os.path.basename(file_path))
            shutil.move(file_path, new_file_path)

    # Ask user if they want to repeat the process
    repeat = input("Do you want to repeat the process? (yes/no): ").lower()
    if repeat != 'yes':
        break
