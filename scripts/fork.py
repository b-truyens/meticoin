import os
import codecs

def replace_words_in_files(root_dir, word_pairs):
    change_count = 0
    # First replace in files
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        if ".git" in dirpath:
            continue

        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            with codecs.open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                lines = file.readlines()

            with codecs.open(filepath, 'w', encoding='utf-8') as file:
                for line in lines:
                    for old_word, new_word in word_pairs.items():
                        count = line.count(old_word)
                        change_count += count
                        line = line.replace(old_word, new_word)
                    file.write(line)

    print(f"Total changes made in files: {change_count}")

    # Then replace in file and directory names
    change_count = 0
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        if ".git" in dirpath:
            continue

        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            for old_word, new_word in word_pairs.items():
                if old_word in filename:
                    new_file_path = os.path.join(dirpath, filename.replace(old_word, new_word))
                    os.rename(filepath, new_file_path)
                    change_count += 1

        for dirname in dirnames:
            dir_full_path = os.path.join(dirpath, dirname)
            for old_word, new_word in word_pairs.items():
                if old_word in dirname:
                    new_dir_path = os.path.join(dirpath, dirname.replace(old_word, new_word))
                    os.rename(dir_full_path, new_dir_path)
                    change_count += 1

    print(f"Total changes made in filenames and directory names: {change_count}")

# Test the function
root_dir = "/home/mpi/meticoin"  # change to your directory
word_pairs = {
    "meticoin": "meticoin", 
    "Meticoin": "Meticoin", 
    "METI": "METI", 
    "meticoind": "meticoind", 
    "Meticoind": "Meticoind", 
    "stuivers": "stuivers", 
    "duiten": "duiten", 
    "Stuivers": "Stuivers", 
    "Duiten": "Duiten", 
    "METICOIN": "METICOIN", 
    "metoshi": "metoshi", 
    "Metoshi": "Metoshi", 
    "metiCoin": "metiCoin", 
    "MetiCoin": "MetiCoin",
    "23230": "23230",
    "23231": "23231",
    "23232": "23232",

    }  # change to your words
replace_words_in_files(root_dir, word_pairs)
