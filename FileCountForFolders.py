import os
import csv

'''
For the file structure:
- Main_Folder
-- Folder_1
--- File_1
--- File_2
--- ...
--- File_n
-- Folder_2
-- ...
-- Folder_m
'''

path = 'path/to/folder/with/more/folders' #Path to Main_Folder

folders = os.listdir(path) #Lists all subfolders within Main_Folder

for file in folders:
    newPath = path +"/" + file #Creates new file path for each subfolder
    print("{}\t\t\t{}".format(file,len(os.listdir(newPath)))) #prints subfolder and number of files
        
    
