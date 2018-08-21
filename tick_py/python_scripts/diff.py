"""
tick diff-
couts the diffrence between last 2 commits.
"""
import os
import zipfile
current = os.getcwd()
os.chdir('.tick/commits')
sorted_a = sorted( os.listdir('.'), key=os.path.getmtime)
os.chdir(current)
for i in sorted_a:
        if i[-3:] != 'zip':
            sorted_a.remove(i)
    

#make an test area to unzip the compressed files
#to perform diffs
try:
    os.mkdir('.tick/diff')
    os.mkdir('.tick/diff/'+sorted_a[-1])
    os.mkdir('.tick/diff/'+sorted_a[-2])
except FileExistsError:
    shutil.rmtree(os.mkdir('.tick/diff'))

    os.mkdir('.tick/diff')
    os.mkdir('.tick/diff/'+sorted_a[-1])
    os.mkdir('.tick/diff/'+sorted_a[-2])

latest = zipfile.ZipFile('.tick/commits/'+sorted_a[-2],'r')
latest.extractall('.tick/diff/'+sorted_a[-2])
latest.close()
second_latest = zipfile.ZipFile('.tick/commits/'+sorted_a[-1],'r')
second_latest.extractall('.tick/diff/'+sorted_a[-1])
second_latest.close()
all_file1=[]
all_file2=[]
loop=0
