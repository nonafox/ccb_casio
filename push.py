import os
import shutil

drive = 'E:'
rsc = '.\\ccb\\'
dest = f'{drive}\\ccb\\'

shutil.rmtree(dest)
os.mkdir(dest)
for root, dirs, files in os.walk(rsc):
    for file in files:
        file_path = os.path.join(root, file)
        if (file.split('.')[- 1] != 'pyi'):
            shutil.copy2(file_path, os.path.join(dest, file_path.replace(rsc, '')))
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        os.mkdir(os.path.join(dest, dir_path.replace(rsc, '')))
print('* Pushing succeeded!')
