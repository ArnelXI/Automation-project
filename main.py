import os

#going through every file in the Directories: Desktop, Documents, Download

list_directory = ["Desktop","Documents","Download"]

#Photo File Formats: JPEG, GIF, PNG, TIFF, BMP.
#Music File Formats: AAC, MP3, WAV, WMA, DOLBY® DIGITAL, DTS.
for directory in list_directory:
    for file in os.listdir(directory):
        filename  = os.fsdecode(file)
