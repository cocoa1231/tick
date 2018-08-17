import os 
import zipfile
import hashlib
import logging
import shutil
import json
import ast

zip_files=[]
#package commit message 
def commit(message):
    try:    
        shutil.rmtree('.tick/staging/')
    except FileNotFoundError:
        print("Nothing to commit")        
        exit()

    
    for i in os.listdir('.tick/commits'):
        if i[-3:] == "zip":
            zip_files.append(i)
    
    sha = hashlib.sha1(str(str(message)+str(len(zip_files))).encode()).hexdigest()
    
    commit_zip = zipfile.ZipFile('.tick/commits/'+sha+'.zip', 'w')
    for folder, subfolders, files in os.walk('.tick/staging'):
        for file in files:
            commit_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), '.tick/staging'), compress_type = zipfile.ZIP_DEFLATED)
    
    commit_zip.close()      
    
    data={"sha":sha,"message":message}
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('.tick/commits/commit.log')
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.info(str(data))

#TODO Files on basis of date