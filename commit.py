import os 
import zipfile
import hashlib
import shutil

def commit(message):
    commit_zip = zipfile.ZipFile('.tick/commits/'+hashlib.sha1(message.encode()).hexdigest()+'.zip', 'w')
    for folder, subfolders, files in os.walk('.tick/staging'):
 
        for file in files:
            commit_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), '.tick/staging'), compress_type = zipfile.ZIP_DEFLATED)
 
    commit_zip.close()         
    
    shutil.rmtree('.tick/staging/')    