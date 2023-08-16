

import os

# returns the subfolders and the files that contain the extension
# got it from https://stackoverflow.com/a/59803793
# dir: str, ext: list
def run_fast_scandir(dir, ext):
    
    subfolders, files = [], []
    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in ext:
                files.append(f.path)
    #
    for dir in list(subfolders):
        sf, f = run_fast_scandir(dir, ext)
        subfolders.extend(sf)
        files.extend(f)
    #
    return subfolders, files

test = run_fast_scandir('path', '.py')

