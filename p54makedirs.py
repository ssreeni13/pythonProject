import os
try:
    os.makedirs("e:\dir1/df1")
    print("Folder Created--Verify")
except FileExistsError:
    print("Folder was already created,It can't create again")
