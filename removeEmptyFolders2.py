import os
import browseButton
def removeEmptyFolders():
    #Removes Empty folders and subfolders
    
    path = str(browseButton.filename)
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