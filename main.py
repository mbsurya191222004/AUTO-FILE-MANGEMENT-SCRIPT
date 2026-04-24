import os
import shutil
import pathlib
import time

source = '/home/kashi/Downloads'
pre_source='/home/kashi/Downloads'

img= ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp', '.ico', '.heic', '.heif']
vid=['.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv', '.webm', '.mpeg', '.mpg', '.3gp', '.m4v', '.ts', '.vob']
aud=['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.alac', '.aiff', '.amr', '.opus']
prog=['.exe', '.bat', '.sh', '.py', '.js', '.jar', '.pl', '.rb', '.php', '.cpp', '.c', '.cs', '.java', '.go', '.swift', '.rs', '.out']
doc= ['.doc', '.docx', '.pdf', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx', '.csv', '.epub', '.pages', '.md']
compressed = ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.tar.gz', '.tgz', '.tar.bz2', '.tbz2', '.tar.xz', '.txz', '.lz', '.lzma', '.z', '.cab', '.iso', '.dmg', '.apk']

def init():
    folders = ["imgs", "videos", "documents", "programs", "audio","compressed"]

    for folder in folders:
        path = f"{pre_source}/{folder}"
        if not os.path.exists(path):
            os.mkdir(path)

def sort_files():

    allfiles = os.listdir(source)

    for i in allfiles:
        file_extension = pathlib.Path(i).suffix

        
        if file_extension in img:
            shutil.move(f"{source}/{i}",f"{pre_source}/imgs")
        elif file_extension in doc:
            shutil.move(f"{source}/{i}",f"{pre_source}/documents")
        elif file_extension in prog:
            shutil.move(f"{source}/{i}",f"{pre_source}/programs")
        elif file_extension in aud:
            shutil.move(f"{source}/{i}",f"{pre_source}/audio")
        elif file_extension in vid:
            shutil.move(f"{source}/{i}",f"{pre_source}/videos")
        elif file_extension in compressed:
            shutil.move(f"{source}/{i}",f"{pre_source}/compressed")
        else:
            pass

init()
while True:
    sort_files()
    time.sleep(3)
  
        