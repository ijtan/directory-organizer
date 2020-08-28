#should be quite a simple program thus one class should suffice
import os,sys,shutil
from pathlib import Path
downloadsPath = Path("D:/Downloads/test")

docs = ['.pdf','.docx','.doc','.pptx','.ppt','.pps','.odp','.rtf'] 
data = ['.csv','.txt','.json','.yaml','.xlsx','.xls','.xlsm','.sql','.html','.data','.xml','.cfg']
media = ['.png','.jpg','.mp3','.mp4','.m4v','.mkv','.swf','.flv','.avi','.gif','.wav','.bmp','.jpeg','.ico','.ps','.psd','.svg']
archives = ['.zip','.xz','.rar','.7z','.iso'] 
executables = ['.exe', '.msi', '.jar', '.py',
               '.js', '.bat', '.c', '.cpp', '.h', '.torrent']


structure = ['Documents','Data','Media','Archives','Executables','Other']
ignore = ['Torrents']#whole file -> name+ext
def createFolders():
    os.chdir(downloadsPath)
    for fold in structure:
        os.makedirs(fold, exist_ok=True)
def sort():
    cwd = os.getcwd()
    os.chdir(downloadsPath)
    for file in os.listdir(downloadsPath):
        print(f'Processing: {file}')
        filename, file_extension = os.path.splitext(file)
        if filename in structure and file_extension == "":
            continue
        elif file in ignore:
            continue
        elif file_extension in docs:
            shutil.move(file, downloadsPath / 'Documents' )
        elif file_extension in data:
            shutil.move(file,  downloadsPath / 'Data')
        elif file_extension in media:
            shutil.move(file, downloadsPath / 'Media')
        elif file_extension in archives:
            shutil.move(file, downloadsPath / 'Archives')
        elif file_extension in executables:
            shutil.move(file, downloadsPath / 'Executables')
        else:
            shutil.move(file,  downloadsPath / 'Other')
    os.chdir(cwd)

def needsSorting():
    dirCount = len([dir for dir in os.listdir(downloadsPath) if dir not in ignore])
    itemCount = len(structure)
    return (True if dirCount > itemCount else False)


if needsSorting():
    createFolders()
    sort()
else:
    print("no sorting needed")