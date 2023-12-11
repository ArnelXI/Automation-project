import os
import shutil

#going through every file in the Directories: Desktop, Documents, Download

list_directory = ["Desktop","Documents","Downloads"]
#list of all music moved
music_name = []
#list of all video moved
video_name = []
#list of all pictures moved
pictures_name = []

#Photo File Formats: JPEG, GIF, PNG, TIFF, BMP.
#Music File Formats: AAC, MP3, WAV, WMA, DOLBY® DIGITAL, DTS.
for directory in list_directory:
    for file in os.listdir("/Users/Yv-Arnel/"+directory):
        filename  = os.fsdecode(file)
        if filename.endswith(".jpeg") or filename.endswith(".gif") or filename.endswith(".png") or filename.endswith(".tiff") or filename.endswith("BMP"):
            #move to photo Dirrectory
            shutil.move("/Users/Yv-Arnel/"+directory+"/"+filename,"/Users/Yv-Arnel/Pictures")
            pictures_name.append(filename)
        elif filename.endswith(".aac") or filename.endswith(".mp3") or filename.endswith(".wav") or filename.endswith(".wma") or filename.endswith(".DOLBY") or filename.endswith(".DIGITAL"):
            #move to videos Directory
            shutil.move("/Users/Yv-Arnel/"+directory+"/"+filename,"/Users/Yv-Arnel/Movies")
            video_name.append(filename)
        elif filename.endswith(".3g2") or filename.endswith(".3gp") or filename.endswith(".3gpp") or filename.endswith(".asf") or filename.endswith(".avi") or filename.endswith(".dat") or filename.endswith(".dv") or filename.endswith(".divx") or filename.endswith(".f4v") or filename.endswith(".flv") or filename.endswith(".m2ts") or filename.endswith(".m4v") or filename.endswith(".mkv") or filename.endswith(".mod") or filename.endswith(".mov") :
            #move to music Directory
            shutil.move("/Users/Yv-Arnel/"+directory+"/"+filename,"/Users/Yv-Arnel/Music")
            music_name.append(filename)
#/Users/Yv-Arnel/Desktop/Screenshot 2023-12-09 at 15.28.29.png