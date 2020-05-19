from os import listdir, mkdir, getcwd, replace
from os.path import isfile, abspath
from shutil import copy, move



def getfiles():
    a = listdir()
    folders = []
    files = []
    for x in a:
        if "py" in x:
            a.remove(x)
        elif not isfile(x):
            folders.append(x)
        elif isfile(x):
            files.append(x)
    return files,folders

def splittype(files):
    templist = []
    for x in files:
        templist.append(x.split("."))
    templist.sort()
    return templist

def createfolder(foldername):
    try:
        mkdir(foldername)
    except FileExistsError:
        pass
    
def indivfolders(files):
    print("Creating individual folders")
    for x in files:
        try:
            createfolder(x[1])
        except:
            pass

def copyfiles(files):
    print("Copying files to folders")
    sep = "."
    for x in files:
        copy("./"+str(sep.join(x)),"./"+x[len(x)-1])

def movefiles(files):
    print("Moving files to folders")
    sep = "."
    for x in files:
        try:
            move("./"+str(sep.join(x)),"./"+x[len(x)-1])
        except:
            print("File already in destination: " +  str(sep.join(x)))
        
    

def sortfiles():
    files,folders = getfiles()
    print("There are " + str(len(files)) + " files and " + str(len(folders)) + " folders")
    
    if len(files) != 0:
        files = splittype(files)
        indivfolders(files)
        movefiles(files)
        
    
sortfiles()


