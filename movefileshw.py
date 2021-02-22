import os
import shutil
source = input("What is Your source?: ")
dest = input("What is Your destination??: ")
source = source +'/'
dest = dest + '/'
listOfFiles =  os.listdir(source)
for file in listOfFiles: 
    shutil.move((source + file),dest)