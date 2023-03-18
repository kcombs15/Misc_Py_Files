import os
from PIL import Image

# Format: Folder -> Folder -> Files

collection = 'path/to/parent/folder' # Path to the folder with other folders

for root, dirs, files in os.walk(collection):
    for folder in dirs:
        folderPath = root + folder #path to folders
        os.chdir(folderPath) #change directory to folders
        word = str.split(folder,'_')[-1] #get the folder name
        for root1, dirs1, files1 in os.walk(folderPath):
            for i, filename in enumerate(files1):
                if filename[-3] == '.png':
                    pass # if already .png skip
                else:
                    oldPath = folderPath + "/" + filename
                    newPath = folderPath + "/" + word + "_" + str(i+1) + ".png"
                    newPathJpg = folderPath + "/" + word + "_" + str(i+1) + ".jpg"
                    os.rename(oldPath, newPath)
                    img_png = Image.open(newPath)
                    img_rgb = img_png.convert('RGB') #converts from RGBA to RGB
                    img_rgb.save(newPathJpg) #saves as JPG
