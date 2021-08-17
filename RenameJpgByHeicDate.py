# Export photos from Photos Library in both way
# 1. export unmodified into a "original" folder
# 2. export in jpeg into a "exported" folder
# 3. put this script on the same level as the two folders
# 4. open terminal and navigate to the script and run "python Rename.py"

import os.path, time
from datetime import datetime

path = os.getcwd()

print(path)
files = []
files_exported = []
dictFileToDate = {}

for r, d, f in os.walk(path+"/original"):
    for file in f:
        if '.HEIC' in file:
            files.append(file)
        if '.heic' in file:
            files.append(file)
        if '.JPEG' in file:
            files.append(file)
        if '.jpeg' in file:
            files.append(file)
        if '.JPG' in file:
            files.append(file)
        if '.jpg' in file:
            files.append(file)
        if '.PNG' in file:
            files.append(file)
        if '.png' in file:
            files.append(file)
        if '.mp4' in file:
            files.append(file)
        if '.MP4' in file:
            files.append(file)
        if '.MOV' in file:
            files.append(file)
        if '.mov' in file:
            files.append(file)

    print("original file count: ", len(files))

for r, d, f in os.walk(path+"/exported"):
    for file in f:
        if '.JPEG' in file:
            files_exported.append(file)
        if '.jpeg' in file:
            files_exported.append(file)
        if '.JPG' in file:
            files.append(file)
        if '.jpg' in file:
            files.append(file)
        if '.PNG' in file:
            files_exported.append(file)
        if '.png' in file:
            files_exported.append(file)
        if '.mp4' in file:
            files_exported.append(file)
        if '.MP4' in file:
            files_exported.append(file)
        if '.MOV' in file:
            files_exported.append(file)
        if '.mov' in file:
            files_exported.append(file)
    print("exported file count: ", len(files_exported))

for f in files:
    filename = os.path.splitext(f)[0]
    filetime = datetime.fromtimestamp(os.path.getmtime("original/"+f)).strftime('%Y%m%d')
    dictFileToDate[filename] = filetime
    print(filename + " -> last modified on -> " + filetime)

for f in files_exported:
    filename = os.path.splitext(f)[0]
    if filename in dictFileToDate:
        newfilename = dictFileToDate[filename] + "_" + f
        print(f + " -> " + newfilename)
        if os.path.isfile("exported/"+f):
            os.rename("exported/"+f, "exported/"+newfilename)
    else:
        print("!!!!!FFFFFile not found from original dictFileToDate: " + filename)
