import os 
import zipfile
import hashlib
import shutil
import json
import ast

#package commit message 
def commit(message):
    
    
    try:
        if not os.path.exists(".tick/commits/data.json"):

            with open('.tick/commits/data.json','w+') as jsF:
                jsF.write('{"commits":  {"0": "0"}}')
    
        sha = hashlib.sha1(message.encode()).hexdigest()
        commit_zip = zipfile.ZipFile('.tick/commits/'+sha+'.zip', 'w')
        if os.path.exists('.tick/staging'):
            for folder, subfolders, files in os.walk('.tick/staging'):
 
                for file in files:
                    commit_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), '.tick/staging'), compress_type = zipfile.ZIP_DEFLATED)
        else:
            print("No Additions to Commit")
        #close the zip
        commit_zip.close()         

        sha_data={"sha":sha,"message":message}
        #dump json data
        #add to txt first
        #  TODO  : optimize
        # Lol , the lies  I tell myself
    
        with open('.tick/commits/data.txt','r') as f:
            f.write(str(sha_data))
        shutil.rmtree('.tick/staging/')    

    except FileNotFoundError:
        print("Nothing to commit")        
        