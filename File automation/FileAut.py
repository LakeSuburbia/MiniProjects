import os
import glob
import shutil

files_list = glob.glob("/Users/sandermangelschots/Downloads")

extension_set = set()

for file in files_list:
    extension = file.split(".")
    try:
        extension_set.add(extension[1])
    except IndexError:
        continue

print(extension_set)