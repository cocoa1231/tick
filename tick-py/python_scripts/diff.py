import os
current = os.getcwd()
os.chdir('.tick/commits')
sorted_a = sorted( os.listdir('.'), key=os.path.getmtime)
os.chdir(current)
print(sorted_a)