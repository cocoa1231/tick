"""
describe.py

Just a few details for the remote url to get about the repo
"""

import getpass
import os
import json

name=os.getcwd().split('/')[-1]
author = getpass.getuser()

#default input check
def defIn(custom,default):
    var=''
    if len(custom)==0:
        var = default
    else:
        var = custom    
    return var         
    
#ask for details of the repo. 
def describe():
    
    name=defIn(input("Enter Repository Name("+name+"):"),name)
    author=defIn(input("Enter Author Name ("+author+"):"),author)
    describe= {"name":name,"author":author}
    
    with open('.tick/description/data.json', 'w') as outfile:
        json.dump(describe, outfile)
    
    
