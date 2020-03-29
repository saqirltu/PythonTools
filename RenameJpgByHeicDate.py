import os.path, time
from datetime import datetime

path = os.getcwd()

print(path)
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.HEIC' in file:
            files.append(file)

for f in files:
    targetfilename = f.replace(".HEIC", ".jpeg")
    newfilename = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y%m%d-%H%M%S') + ".jpeg"
    print(targetfilename + " -> " + newfilename)
    os.rename(targetfilename, newfilename)
