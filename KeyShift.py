import os
import re
import sys
import subprocess

# Check if tqdm is installed, and if not, install it
try:
    from tqdm import tqdm
except ImportError:
    print("tqdm not found! Installing tqdm...")
    subprocess.run([sys.executable, "-m", "pip", "install", "tqdm"])
    from tqdm import tqdm

def to_raw_string(s):
    return s.encode('unicode_escape').decode()

def has_english(text):
    return bool(re.search('[A-Za-z]', text))

def read_all_txt_files_in_directory(directory):
    all_contents = {}
    files = [f for f in os.listdir(directory) if f.lower().endswith('.txt')]
    for filename in tqdm(files, desc="Reading files"):
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, 'r', encoding='utf8') as f:
                content = f.read()
            all_contents[filepath] = content
        except Exception as e:
            print(f"Error occurred while reading {filepath}: {e}")

    return all_contents

def extract_english_text_from_content(content):
    english_texts = []
    lines = content.splitlines()
    for i in tqdm(range(len(lines) - 1), desc="Extracting English texts"):
        if lines[i].strip() == '[0]' and '1 string data =' in lines[i+1]:
            match = re.search(r'1 string data = "(.*?)"', lines[i+1])
            if match:
                matched_text = match.group(1)
                if has_english(matched_text):
                    english_texts.append(matched_text)
    return english_texts

def save_english_texts_to_txt(texts, filename):
    # Ensure the directory exists
    output_dir = "C:\\OUTPUT FOLDER"  # แก้ไขเส้นทางของไฟล์ให้ถูกต้อง
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_filename = os.path.join(output_dir, "extracted_texts.txt")
    with open(output_filename, 'a', encoding='utf8') as file:
        for text in texts:
            file.write(text + '\n')
    print(f"English texts saved to {output_filename}.")

directory = input("Enter the path to your directory containing txt files: ")
directory = to_raw_string(directory)
all_file_contents = read_all_txt_files_in_directory(directory)

for filepath, content in all_file_contents.items():
    english_texts = extract_english_text_from_content(content)
    
    choice = input(f"Would you like to save the English text from the txt file {filepath} to a txt file? (yes/no) ").strip().lower()
    if choice == 'yes':
        save_english_texts_to_txt(english_texts, filepath)
    elif choice == 'no':
        break
