import os
try:
    os.mkdir("e:\dir1/df1")
    print("Folder Created--Verify")
except FileExistsError:
    print("Folder was already created,It can't create again")
except OSError:
    print("The Hierarchy of Folders unable to create")