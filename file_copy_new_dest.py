#find specific files in folders/sub-folders and copy them to new destination
import os
import shutil

#source and destination paths
folderdir = 'J:\\Torrent_Downloads\\64GB_PS_Classic\\64GB_PSCLASSIC\Games'
dest_folder = 'J:\\Games'

#extensions to look for
ext = ('.bin', '.cue')

#find files that end with extension specified
for path, dirc, files in os.walk(folderdir):
    for name in files:
        if name.endswith(ext):
            print ('Found file in: ' + str(path))
            #copy specifc files from source to destination
            shutil.copy(os.path.abspath(path + '/' + name), dest_folder)