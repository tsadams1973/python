import shutil
import os

fromDirectory = "<from directory>"
toDirecotry = "<to directory>"

# copies from one directory to another; to directory cannot already exist
shutil.copytree(fromDirectory,toDirecotry)

print 'Copied ' + fromDirectory + ' to ' + toDirecotry