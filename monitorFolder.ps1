### SET FOLDER TO WATCH + FILES TO WATCH + SUBFOLDERS YES/NO
    $watcher = New-Object System.IO.FileSystemWatcher
    $watcher.Path = C:\Downloads"
    $watcher.Filter = "*.*"
    $watcher.IncludeSubdirectories = $true
    $watcher.EnableRaisingEvents = $true  

    $action = { 
        #IMPORTANT TO CHANGE & UNCOMMENT:
		start-process pythonw -argument "C:\Users\kinkt\VisualCodeProjects\donloads-folder-organizer\main.py"

              }    
    Register-ObjectEvent $watcher "Created" -Action $action
    Register-ObjectEvent $watcher "Changed" -Action $action
###    Register-ObjectEvent $watcher "Deleted" -Action $action
###    Register-ObjectEvent $watcher "Renamed" -Action $action
    while ($true) {sleep 5}