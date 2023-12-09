import os

#going through every file in the download Directory

list_directory = ["Desktop","Documents","Download"]

for directory in list_directory:
    for file in os.listdir(directory):
        filename  = os.fsdecode(file)
