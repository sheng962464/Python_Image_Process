import os

def GetImageList(FolderPath):
    List_Of_File = []
    if(os.path.isdir(FolderPath)):
        for file in os.listdir(FolderPath):
            List_Of_File.append(os.path.join(FolderPath, file))
