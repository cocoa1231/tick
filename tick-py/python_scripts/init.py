import hashlib
import os
import stage
import commit
import describe
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