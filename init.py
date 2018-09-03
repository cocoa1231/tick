import pyximport; pyximport.install()
import hashlib
import os
import tick.python_scripts.stage as stage
import tick.python_scripts.commit as commit
import tick.python_scripts.describe as describe
import tick.python_scripts.diff as Diff
import getpass
import sys


def init():
    """
    Initialize Repositiory, Log , commit settings
    """
    try:
        os.mkdir(".tick")
        os.mkdir(".tick/description")
    except FileExistsError:
        pass        
    describe.describe()
    
    
    with open("/home/"+getpass.getuser()+"/.colordiff",'w+') as file:
        file.write("""
        # be more git-like:
        plain=off
        newtext=darkgreen
        oldtext=darkred 
        diffstuff=darkcyan
        """)

def stageC(file):
    """
        Staging files for commit
    """
    try:
        os.mkdir(".tick/staging")
    except FileExistsError:
        pass        
    stage.staging(file)

def commitP(message):
    """
    packaging commits
    """
    try:
        os.mkdir(".tick/commits")
    except FileExistsError:
        pass
    
    commit.commit(message)



if sys.argv[1]=="init":
    init()            
elif sys.argv[1]=="add":
    stageC(sys.argv[2])
elif sys.argv[1]=="commit":
    commitP(sys.argv[2])   
elif sys.argv[1] == "diff":
    Diff.tickDiff()     
"""
# be more git-like:
plain=off
newtext=darkgreen
oldtext=darkred
diffstuff=darkcyan




"""