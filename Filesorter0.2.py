
""" Filesortingprogramm """
from tkinter import *
from tkinter import filedialog
import sys
import sortButton
import removeEmptyFolders


def browseButton():
    #Allow user to select a directory and store it in global var
    #called folder_path
    #Also makes global filename for making paths for other functions

    global pathBrowsed
    global filename
    filename = filedialog.askdirectory()
    pathBrowsed.set(filename)
    return filename
    print(filename)


#button enabler to avoid error when pressing buttons in wrong order
def enableButtons():
    buttonSort.config(state=NORMAL)
    buttonRemove.config(state=NORMAL)
    print("Enabled buttons.")

       
#function combiner to execute 2 functions when browse button is pressed
def combineFuncs(*funcs):
    def combinedFunc(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combinedFunc

import os
import shutil

def sortButton():
    #Sort files in browsed directory according to filetype
    
    path = str(filename)
    os.chdir(path)
    
    filesToSort = os.listdir(path)
    print(filesToSort)

    """
    
    t = {i.lower() for i in filesToSort}

    for files in filesToSort:
        if files not in t:
            filesToSort.append(files)
    print(filesToSort)
    """
    
    folderName = ["text", "kalkyl", "DWG", "PDF", "GEO", "Backup"]
    fileType = [".odt", ".ods", ".dwg", ".pdf", ".geo", ".bkp"]
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

def removeEmptyFolders():
    #Removes Empty folders and subfolders
    
    path = str(filename)
    os.chdir(path)
    REMfiles = os.listdir(path)

    

    
    # remove empty subfolders
    if len(REMfiles):
        for files in REMfiles:
            fullpath = os.path.join(path, files)
            """
            for files in fullpath:
                subfullpath = os.path.join(fullpath, files)                                                      
                if os.path.isdir(subfullpath) and len(os.listdir(subfullpath)) == 0:
                    os.rmdir(subfullpath)
                    print("Removed empty folder: " + subfullpath)
            """
                
            if os.path.isdir(fullpath) and len(os.listdir(fullpath)) == 0:
                os.rmdir(fullpath)
                print("Removed empty folder: " + fullpath)
                


    # if folder empty, delete it
    if len(REMfiles) == 0:
        print("Removed empty folder:", path)
        os.rmdir(path)
        removing = path
   
    removing = "Done removing folders."
    print("Done.")



#GUI
root = Tk()
root.title("Filesorter beta 4.0")

labelHeader = Label(root, text="Filesorter")
labelHeader.config(font=("Courier", 25))
labelHeader.grid(row=0 ,column=1)

labelInstruction = Label(root, text="Browse folder to be sorted.")
labelInstruction.config(font=("Courier", 10))
labelInstruction.grid(row=1, column=1)


sortingComplete = StringVar()
labelSorted = Label(master=root,textvariable=sortingComplete)
labelSorted.grid(row=4, column=1)

buttonSort = Button(text="Sort", command=sortButton, state=DISABLED)
buttonSort.grid(row=4, column=2)
                      
removing = StringVar()
labelRemoved = Label(master=root,textvariable=removing)
labelRemoved.grid(row=5, column=1)

buttonRemove = Button(text="Remove empty folders", command=removeEmptyFolders, state=DISABLED)
buttonRemove.grid(row=5, column=2)


buttonBrowse = Button(text="Browse", command=combineFuncs(browseButton, enableButtons))
buttonBrowse.grid(row=3, column=2)
                      
pathBrowsed = StringVar()
labelPath = Label(master=root,textvariable=pathBrowsed)
labelPath.grid(row=3, column=1)

mainloop()
