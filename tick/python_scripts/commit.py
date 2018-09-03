#import pyximport; pyximport.install(pyimport=True)
import os 
import zipfile
import hashlib
import logging
import shutil
from .describe import defIn 


"""
tick commit
compress staged files to save file
"""
zip_files=[]
#package commit message 
def oldFiles():
    current = os.getcwd()
    os.chdir('.tick/commits')
    
    sorted_a = sorted( os.listdir('.'), key=os.path.getmtime)
    os.chdir(current)
    for i in sorted_a:
        if i[-3:] != 'zip':
            sorted_a.remove(i)
    return sorted_a
    

def commit(message):
    
    try:    
        if not os.path.exists('.tick/staging/'):
            raise FileNotFoundError

    except FileNotFoundError:
        print("Nothing to commit")        
        exit()

    
    for i in os.listdir('.tick/commits'):
        if i[-3:] == "zip":
            zip_files.append(i)
    #the line here is not meant for security. Its just identification,really
    sha = hashlib.sha1(str(str(message)+str(len(zip_files))).encode()).hexdigest()

    #compress files
    commit_zip = zipfile.ZipFile('.tick/commits/'+sha+'.zip', 'w')
    for folder, subfolders, files in os.walk('.tick/staging'):
        for file in files:
            commit_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), '.tick/staging'), compress_type = zipfile.ZIP_DEFLATED)
    
    commit_zip.close()      
    shutil.rmtree('.tick/staging')
    #log commits 
    data={"sha":sha,"message":message}
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('.tick/commits/commit.log')
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.info(str(data))
    print(os.getcwd())
    
    if len(oldFiles()) > 2:

        print(os.getcwd())
        sorted_a=oldFiles()        

        result="n"
        result=defIn(input("More that 2 old unpublished commits . Delete to conserve space? (y/n) "),result)   
        print(result)
        if result.strip().lower() == 'y':
            for i in range(len(sorted_a)):
                if i < len(sorted_a)-2:
                    os.remove('.tick/commits/'+sorted_a[i])
        
        else:
            print('aborting removal')


