import hashlib
import os
import tick.python_scripts.stage as stage
import tick.python_scripts.commit as commit
import tick.python_scripts.describe as describe
import sys
"""
Initialize Repositiory, Log , commit settings
"""
def init():
    try:
        os.mkdir(".tick")
        os.mkdir(".tick/description")
    except FileExistsError:
        pass        
    describe.describe()
"""
Staging files for commit
"""
def stageC(file):
    try:
        os.mkdir(".tick/staging")
    except FileExistsError:
        pass        
    stage.staging(file)
"""
packaging commits
"""
def commitP(message):
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