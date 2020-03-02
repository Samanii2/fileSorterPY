import os
import shutil
import browseButton
def sortButton():
    #Sort files in browsed directory according to filetype
    
    path = str(browseButton.filename)
    os.chdir(path)
    
    filesToSort = os.listdir(path)
    print(filesToSort)

    
    folderName = ["text", "text", "text", "kalkyl", "DWG", "PDF", "GEO", "Backup", "Backup"]
    fileType = [".odt", ".txt", "doc", ".ods", ".dwg", ".pdf", ".geo", ".bkp", ".llc"]
    #sets the lenght of loops
    fTL = len(fileType)

    subFolderName = ["PP", "Inmätningar"]
    
    subFileType = ["pp" , "inm"]
    #sets the lenght of loops
    sFTL = len(subFileType)
    

    #List with number of filetypes in boolean used for the sorting algo
    fileTypeChecked = []
    for item in fileType:
        fileTypeChecked.append(False)

    for item in subFileType:
        fileTypeChecked.append(False)
    print(fileTypeChecked)
    
    #Check to see if filesToSort exists in dir before making of folders
    for x in range(fTL):
        for file in filesToSort: 
            if file.endswith(fileType[x]):
                del fileTypeChecked[x]
                fileTypeChecked.insert(x, True)

    #Check to see if filesToSortLower exists in dir before making of folders
    for x in range(sFTL):
        for file in filesToSort:
            if file.startswith(subFileType[x]):
                del fileTypeChecked[fTL + x]
                fileTypeChecked.insert(fTL + x, True)
    
           
    print("Filetypes in directory")
    print(fileType + subFileType)
    print(fileTypeChecked)    
        
    #Make folders of folderName for fileTypes
    for x in range(fTL):
        if not os.path.exists(path + '/' + folderName[x]) and os.path.basename(path) != folderName[x] and fileTypeChecked[x] == True:
            os.makedirs(path + '/' + folderName[x])
            print("Created folder: " + path + '/' + folderName[x]) 
          
    #Make folders of subFolderName for subFileTypes
    for x in range(sFTL):
        if not os.path.exists(path + '/GEO/' + subFolderName[x]) and fileTypeChecked[fTL + x] == True:
            os.makedirs(path + '/GEO/' + subFolderName[x])
            print("Created subfolder: " + path + '/GEO/' + subFolderName[x])
    

    #Move files from filesToSort into folders folderName
    for x in range(fTL):
        for files in filesToSort:
            if fileType[x] in files and not os.path.exists(path + '/' + folderName[x] + '/' + files):
                shutil.move(path + '/' + files, path + '/' + folderName[x] + '/')
                print("Moved file: " + path + '/' + files)
    
    for x in range(sFTL):
        for files in filesToSort:
            if subFileType[x] in files and not os.path.exists(path + '/GEO/' + subFolderName[x] + '/' + files):
                shutil.move(path + '/GEO/' + files, path + '/GEO/' + subFolderName[x] + '/')
                print("Moved file: " + path + '/' + files)
    
    sortingComplete = "Done"
    print("Files sorted.")
