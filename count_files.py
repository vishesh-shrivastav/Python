import os
count = 0
path = 'C:/Users/vishesh.vishesh/Desktop/New folder'
os.chdir(path)
cwd = os.getcwd()
for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       if filename.endswith('.txt') :
           count += 1
print (cwd)           
print ('Files:', count)
