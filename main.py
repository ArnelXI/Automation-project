import os
import shutil

#going through every file in the Directories: Desktop, Documents, Download
path = "/Users/your-username/"
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
    for file in os.listdir(path+directory):
        filename  = os.fsdecode(file)
        if filename.endswith(".jpeg") or filename.endswith(".gif") or filename.endswith(".png") or filename.endswith(".tiff") or filename.endswith("BMP"):
            #move to photo Dirrectory
            shutil.move(path+directory+"/"+filename,path+"Pictures")
            pictures_name.append(filename)
        elif filename.endswith(".aac") or filename.endswith(".mp3") or filename.endswith(".wav") or filename.endswith(".wma") or filename.endswith(".DOLBY") or filename.endswith(".DIGITAL"):
            #move to videos Directory
            shutil.move(path+directory+"/"+filename,path+"Movies")
            video_name.append(filename)
        elif filename.endswith(".3g2") or filename.endswith(".3gp") or filename.endswith(".3gpp") or filename.endswith(".asf") or filename.endswith(".avi") or filename.endswith(".dat") or filename.endswith(".dv") or filename.endswith(".divx") or filename.endswith(".f4v") or filename.endswith(".flv") or filename.endswith(".m2ts") or filename.endswith(".m4v") or filename.endswith(".mkv") or filename.endswith(".mod") or filename.endswith(".mov") :
            #move to music Directory
            shutil.move(path+directory+"/"+filename,path+"Music")
            music_name.append(filename)
print("We have moved: {0} Image".format(len(pictures_name)))
for image in pictures_name:
    print(image+"/n")
print("We have moved: {0} Videos".format(len(video_name)))
for video in video_name:
    print(video+"/n")
print("We have moved: {0} Music".format(len(music_name)))
for music in music_name:
    print(music_name+"/n")