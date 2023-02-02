#should be quite a simple program thus one class should suffice
import os,sys,shutil
from pathlib import Path
import argparse
import subprocess
from time import sleep



parser = argparse.ArgumentParser(description="Directory Sorter")
parser.add_argument("--dir")
args, leftovers = parser.parse_known_args()


docs = ['.pdf','.docx','.doc','.pptx','.ppt','.pps','.odp','.rtf'] 
data = ['.csv','.txt','.json','.yaml','.xlsx','.xls','.xlsm','.sql','.html','.data','.xml','.cfg', '.log', '.bib']
media = ['.png','.jpg','.mp3','.mp4','.m4v','.mkv','.swf','.flv','.avi','.gif','.wav','.webm','.bmp','.jpeg','.ico','.ps','.psd','.svg']
archives = ['.zip', '.xz', '.rar', '.7z', '.iso', '.tar', '.gz']
executables = ['.exe', '.msi', '.jar', '.bat', '.torrent', '.apk', '.bin', '.deb', '.AppImage', '.dmg', '.pkg', '.rpm', '.run', '.sh', '.msi', '.msix', '.msixbundle']
code = ['.ipynb', '.py', '.js', '.c', '.cpp', '.h','.lua', '.class', '.java', '.php', '.vb', '.html', '.css', '.svelte', '.ts', '.tsx', '.go', '.rb', '.rs', '.swift', '.kt', '.kts', '.dart', '.asm', '.asmx', '.aspx', '.cs', '.cshtml', '.csproj', '.csx', '.fs', '.fsx', '.vb', '.vbhtml', '.vbproj', '.vbs', '.xaml', '.xaml.cs', '.xaml.vb', '.xaml.csproj', '.xaml.vbproj', '.xaml.csproj.user', '.xaml.vbproj.user', '.xaml.csproj.vspscc', '.xaml.vbproj.vspscc', '.xaml.csproj.vspscc.bak', '.xaml.vbproj.vspscc.bak', '.xaml.csproj.user.bak', '.xaml.vbproj.user.bak', '.xaml.csproj.user.vspscc', '.xaml.vbproj.user.vspscc', '.xaml.csproj.user.vspscc.bak', '.xaml.vbproj.user.vspscc.bak', '.xaml.csproj.vspscc', '.xaml.vbproj.vspscc', '.xaml.csproj.vspscc.bak', '.xaml.vbproj.vspscc.bak', '.xaml.csproj.user', '.xaml.vbproj.user', '.xaml.csproj.user.bak', '.xaml.vbproj.user.bak', '.xaml.csproj.user.vspscc', '.xaml.vbproj.user.vspscc', '.xaml.csproj.user.vspscc.bak', '.xaml.vbproj.user.vspscc.bak', '.xaml.csproj.vspscc', '.xaml.vbproj.vspscc', '.xaml.csproj.vspscc.bak', '.xaml.vbproj.vspscc.bak', '.xaml.csproj.user', '.xaml.vbproj.user', '.xaml.csproj.user.bak', '.xaml.vbproj.user.bak', '.xaml.csproj.user.vspscc', '.xaml.vbproj.user.vspscc', '.xaml.csproj.user.vspscc.bak', '.xaml.vbproj.user.vspscc.bak', '.xaml.csproj.vspscc', '.xaml.vbproj.vspscc', '.xaml.csproj.vspscc.bak']

structure = ['Documents','Data','Media','Archives','Executables','Coding','Other']
ignore = ['Torrents']#whole file -> name+ext
ignoreExt = ['.crdownload','.tmp','.opdownload'] # extensions to ignore
loc = ""

def createFolders():
    os.chdir(sortingPath)
    for fold in structure:
        os.makedirs(fold, exist_ok=True)

def sort():
    global loc
    global movedTo
    cwd = os.getcwd()
    os.chdir(sortingPath)
    for file in os.listdir(sortingPath):
        print(f'Processing: {file}')
        filename, file_extension = os.path.splitext(file)
        if filename in structure and file_extension == "":
            continue
        elif file in ignore or file_extension in ignoreExt:
            continue
        elif file_extension in docs:
            dest  = sortingPath / 'Documents';
        elif file_extension in data:
           dest =   sortingPath / 'Data'
        elif file_extension in media:
            dest = sortingPath / 'Media'
        elif file_extension in archives:
            dest = sortingPath / 'Archives'
        elif file_extension in executables:
            dest = sortingPath / 'Executables'
        elif file_extension in code:
            dest = sortingPath / 'Coding'
        else:
            dest =  sortingPath / 'Other'

        if os.path.exists(dest) and os.path.isdir(dest):  # if folder exists
            
            i = 0
            new_name = filename + file_extension
            while os.path.exists(dest / new_name):
                new_name = filename + "_" + str(i) + file_extension
                i+=1
            os.rename(file, new_name)
            file = new_name
        shutil.move(file, dest)
        # movedTo = dest
        # print(f'set movedto to: {movedTo}')
        if(os.name == 'nt'):
            # print('nt')
            # if movedTo != "":
                # print('opening: ',end=' ')
            loc = str(dest).rsplit(',', 1)[-1]+'\\'
            print('opening loc:', loc)
            os.startfile(loc)
            # print(['explorer /select,"'+loc+'\\"'])
            # subprocess.Popen(['explorer /select,"'+loc+'\\"'])
                # sleep(5)
        
    os.chdir(cwd)

def needsSorting():
    dirCount = len([dir for dir in os.listdir(sortingPath) if dir not in ignore])
    itemCount = len(structure)
    return (True if dirCount > itemCount else False)

def checkPath():
    if sortingPath.is_dir():
        print(f"Sorting Directory: '{sortingPath}'")
    else:
        print("Download Path specified does not exist!")
        exit()


sortingPath = (Path("test") if args.dir is None else Path(args.dir))
def run():
    checkPath()        
    if needsSorting():
        createFolders()
        print('sorting')
        sort()
    else:
        print("no sorting needed")

def open_path():
    global loc
    print(['explorer', str(loc)])
    subprocess.Popen(['explorer', str(loc)])

run()

    # movedTo = ""   
if(os.name=='nt'):
    from win10toast_click import ToastNotifier 
    toaster = ToastNotifier()
    # toaster.show_toast("Directory Sorter", "done sorta")

    toaster.show_toast(
        "Directory Sorter",  # title
        "Done Sorting!",  # message
        icon_path=None,  # 'icon_path'
        duration=5,  # for how many seconds toast should be visible; None = leave notification in Notification Center
        threaded=True,  # True = run other code in parallel; False = code execution will wait till notification disappears
        callback_on_click=open_path  # click notification to run function
    )
 


    # if movedTo:
    #toaster.show_toast("Directory Sorter", "File was moved to: "+ movedTo)
    
