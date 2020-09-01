### SET FOLDER TO WATCH + FILES TO WATCH + SUBFOLDERS YES/NO
    $watcher = New-Object System.IO.FileSystemWatcher
    #$watcher.Path = "D:\Downloads" # uncomment & update this to point to watch directory

    $watcher.Filter = "*.*"
    $watcher.IncludeSubdirectories = $true
    $watcher.EnableRaisingEvents = $true  

    $action = { 
        #IMPORTANT TO CHANGE & UNCOMMENT:
		#start-process pythonw -argument "<add path to main.py script here>"

              }    
    Register-ObjectEvent $watcher "Created" -Action $action
    Register-ObjectEvent $watcher "Changed" -Action $action
###    Register-ObjectEvent $watcher "Deleted" -Action $action
###    Register-ObjectEvent $watcher "Renamed" -Action $action
    while ($true) {sleep 5}