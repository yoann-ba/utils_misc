

from zipfile import ZipFile


path = 'path to zip file'


archive = ZipFile(path, 'r')
files = archive.namelist() # list of file names inside the zip

# extract just specific files from the zip
for file_name in files:
    new_local_file = archive.extract(file_name)



