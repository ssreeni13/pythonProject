import os
try:
    os.rmdir("e:\dir1/df1")
    print("Folder Removed--Verify")
except FileNotFoundError:
    print("Folder Name doesn't Exists")
except OSError:
    print("Specified Folder Contains files, Can't be Removed")