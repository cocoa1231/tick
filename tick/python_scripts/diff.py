"""
tick diff-
couts the diffrence between last 2 commits.

"""


import os
import shutil
import zipfile
from subprocess import call

def tickDiff():
    """
    code for tick diff

    """
    current = os.getcwd()
    os.chdir('.tick/commits')
    sorted_a = sorted( os.listdir('.'), key=os.path.getmtime)
    os.chdir(current)
    for i in sorted_a:
            if i[-3:] != 'zip':
                sorted_a.remove(i)


    #make an test area to unzip the compressed files
    #to perform diffs
    #temporary

    try:
        os.mkdir('.tick/diff')
    except FileExistsError:
        pass
    try:
        os.mkdir('.tick/diff/'+sorted_a[-1])
    except FileExistsError:
        pass        
    try:
        os.mkdir('.tick/diff/'+sorted_a[-2])
    except FileExistsError:
        pass        

    latest = zipfile.ZipFile('.tick/commits/'+sorted_a[-2],'r')
    latest.extractall('.tick/diff/'+sorted_a[-2])
    latest.close()
    second_latest = zipfile.ZipFile('.tick/commits/'+sorted_a[-1],'r')
    second_latest.extractall('.tick/diff/'+sorted_a[-1])
    second_latest.close()
    call(['colordiff','-r','-u','.tick/diff/'+sorted_a[-1],'.tick/diff/'+sorted_a[-2]])
    shutil.rmtree('.tick/diff')
