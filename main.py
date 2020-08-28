#should be quite a simple program thus one class should suffice
import os,sys,shutil
from pathlib import Path
import argparse


parser = argparse.ArgumentParser(description="Directory Sorter")
parser.add_argument("--dir")
args, leftovers = parser.parse_known_args()


docs = ['.pdf','.docx','.doc','.pptx','.ppt','.pps','.odp','.rtf'] 
data = ['.csv','.txt','.json','.yaml','.xlsx','.xls','.xlsm','.sql','.html','.data','.xml','.cfg']
media = ['.png','.jpg','.mp3','.mp4','.m4v','.mkv','.swf','.flv','.avi','.gif','.wav','.bmp','.jpeg','.ico','.ps','.psd','.svg']
archives = ['.zip','.xz','.rar','.7z','.iso'] 
executables = ['.exe', '.msi', '.jar', '.py',
               '.js', '.bat', '.c', '.cpp', '.h', '.torrent']

structure = ['Documents','Data','Media','Archives','Executables','Other']
ignore = ['Torrents']#whole file -> name+ext

def createFolders():
    os.chdir(sortingPath)
    for fold in structure:
        os.makedirs(fold, exist_ok=True)
def sort():
    cwd = os.getcwd()
    os.chdir(sortingPath)
    for file in os.listdir(sortingPath):
        print(f'Processing: {file}')
        filename, file_extension = os.path.splitext(file)
        if filename in structure and file_extension == "":
            continue
        elif file in ignore:
            continue
        elif file_extension in docs:
            shutil.move(file, sortingPath / 'Documents' )
        elif file_extension in data:
            shutil.move(file,  sortingPath / 'Data')
        elif file_extension in media:
            shutil.move(file, sortingPath / 'Media')
        elif file_extension in archives:
            shutil.move(file, sortingPath / 'Archives')
        elif file_extension in executables:
            shutil.move(file, sortingPath / 'Executables')
        else:
            shutil.move(file,  sortingPath / 'Other')
    os.chdir(cwd)

def needsSorting():
    dirCount = len([dir for dir in os.listdir(sortingPath) if dir not in ignore])
    itemCount = len(structure)
    return (True if dirCount > itemCount else False)

def checkPath():
    if sortingPath.exists():
        print(f"Sorting Directory: '{sortingPath}'")
    else:
        print("Download Path specified does not exist!")
        exit()


sortingPath = (Path("test") if args.dir is None else args.dir)
def run():
    checkPath()        
    if needsSorting():
        createFolders()
        sort()
    else:
        print("no sorting needed")
    
run()

