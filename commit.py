import os 
import zipfile
import hashlib
import shutil

def commit(message):
    sha = hashlib.sha1(message.encode()).hexdigest()
    commit_zip = zipfile.ZipFile('.tick/commits/'+sha+'.zip', 'w')
    if os.path.exists('.tick/staging'):
        for folder, subfolders, files in os.walk('.tick/staging'):
 
            for file in files:
                commit_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), '.tick/staging'), compress_type = zipfile.ZIP_DEFLATED)
    else:
        print("Nothing to Commit")
    commit_zip.close()         
    os.mkdir(".tick/staging/commits/logs")
    data={"sha":sha,"message":message}
    with open('.tick/commits/data.json', 'w') as outfile:
        json.dump(data, outfile)
    shutil.rmtree('.tick/staging/')    