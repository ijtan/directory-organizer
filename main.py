#should be quite a simple program thus one class should suffice
import os,sys,shutil
from pathlib import Path
downloadsPath = Path("C:\Downloads\SortTest")

docs = ['.pdf','.docx','.doc','.pptx','.ppt','.pps','.odp','.rtf'] #split into presentations/pdfs and txt files
data = ['.csv','.txt','.json','.yaml','.xlsx','.xls','.xlsm','.sql','.html','.data','.xml','.cfg']
media = ['.png','.jpg','.mp3','.mp4','.m4v','.mkv','.swf','.flv','.avi','.gif','.wav','.bmp','.jpeg','.ico','.ps','.psd','.svg']
archives = ['.zip','.tar.xz','.rar','.7z','.iso'] #check for xz then check for a 'tar' before it
runnables = ['.exe','.msi','.jar','.py','.js','.bat','.c','.cpp','h'] 
torrents = ['.torrent']

structure = ['Documents','Data','Media','Archives','Runnables','Other','Torrents']
ignore = []
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
        if filename in ignore:
            continue
        if file_extension in docs:
            shutil.move(file, downloadsPath / 'Documents' )
        elif file_extension in data:
            shutil.move(file,  downloadsPath / 'Data')
        elif file_extension in media:
            shutil.move(file, downloadsPath / 'Media')
        elif file_extension in archives:
            shutil.move(file, downloadsPath / 'Archives')
        elif file_extension in runnables:
            shutil.move(file, downloadsPath / 'Runnables')
        elif file_extension in torrents:
            shutil.move(file,  downloadsPath / 'Torrents')
        else:
            shutil.move(file,  downloadsPath / 'Other')
    os.chdir(cwd)

def checkChange():
    if change:
        createFolders()
        sort()
def CheckChange:
    