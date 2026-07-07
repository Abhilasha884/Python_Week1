import os

'''to get current directory'''
cwd=os.getcwd()
'''to create a directory at specified path'''
os.mkdir()
'''os.listdir() method returns a list of files and directories in the specified path. If no path is provided, it lists the contents of the current working directory.'''
os.listdir(path)
'''To remove the directory'''
os.remove()
''' used to remove or delete an empty directory. OSError will be raised if the specified path is not an empty directory'''
os.rmdir()
'''to change the permission'''
os.chmod()
print("Current working directory: ",cwd)



