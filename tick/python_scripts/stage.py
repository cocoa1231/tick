"""
Staging - 
Staging area for commits,
Cleared after every commit
"""
import os
import shutil
from distutils.dir_util import copy_tree
"""
stage files 
    
"""
def staging(files):
    try:
        #loop through files
        for file in os.listdir(files):
            #ignore .tick
            if file != ".tick":   
                #for directories TODO: Optomise
                if os.path.isdir(file):
                    if file  not in os.listdir('.tick/staging/'):
                        os.mkdir(".tick/staging/"+file)
                        copy_tree(file, ".tick/staging/"+file)
                        print("staging ->"+file)
                    else:
                        print("Already staged ->"+file)                        
                #for files
                else:
                    if file  not in os.listdir('.tick/staging/'):
                        shutil.copy(file,".tick/staging/")
                        print("staging ->"+file)
                    else :
                        print("Already staged ->"+file)                        
    #for individual files eg. tick add 1.txt
    except NotADirectoryError:
        if files not in os.listdir('.tick/staging'):
            shutil.copy(files,".tick/staging")                        
            print("staging ->"+files)

        else:
            print("already staged file ->"+ files)